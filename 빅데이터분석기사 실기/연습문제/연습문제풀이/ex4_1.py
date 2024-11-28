import pandas as pd

X_train=pd.read_csv('../FIFA_X_train.csv',encoding='CP949')
X_test=pd.read_csv('../FIFA_X_test.csv',encoding='CP949')
y_train=pd.read_csv('../FIFA_y_train.csv',encoding='CP949')
y_test=pd.read_csv('../FIFA_y_test.csv',encoding='CP949')

ID=y_test.ID
X_train.drop(columns='ID',inplace=True)
X_test.drop(columns='ID',inplace=True)
y_train.drop(columns='ID',inplace=True)
y_test.drop(columns='ID',inplace=True)

#print(X_train.info())
#print(X_train.head())

# * 처리된 나이 확인
# cnt=0
# for i in X_train.Age:
#     if '*' in i:
#         print(i)
#         cnt+=1
#print(cnt)

# * 처리된 나이 370개

#print(X_train.isna().sum())

#print(X_test.isna().sum())

# Position_Class 결측값 처리
def position_class(df):
    nondf=df[df['Position_Class'].isna()]
    for i in nondf.index:
        if df.loc[i,'Position'] in ['LS','ST','RS','LW','LF','CF','RF','RW']:
            df.loc[i,'Position_Class']='Forward'
        elif df.loc[i,'Position'] in ['LAM',"CAM",'RAM','LM','LCM','CM','RCM','RM']:
            df.loc[i,'Position_Class']='Midfielder'
        elif df.loc[i,'Position'] in ['LWB','LDM','CDM','RDM','RWB','LB','LCB','CB','RCB','RB']:
            df.loc[i,'Position_Class']='Defender'
        elif df.loc[i,'Position'] in ['GK']:
            df.loc[i,'Position_Class']='GoalKeeper'
    return df


X_train=position_class(X_train)
X_test=position_class(X_test)

X_train.drop(columns=['Position'],inplace=True)
X_test.drop(columns=['Position'],inplace=True)

# Height_cm 결측치 처리
def height_cm(df):
    nondf=df[df['Height_cm'].isna()]
    for i in nondf.index:
        h=df.loc[i,'Height']
        h_list=h.split("'")
        h_list=list(map(float,h_list))
        df.loc[i,'Height_cm']=h_list[0]*30 + h_list[1]*2.5
    return df

X_train=height_cm(X_train)
X_test=height_cm(X_test)

X_train.drop(columns=['Height'],inplace=True)
X_test.drop(columns=['Height'],inplace=True)

cond=X_train['Weight_lb'].isna()

# Weight_lb 는 train에만 결측치가 잇으므로 삭제
y_train=y_train[~cond]
X_train.dropna(inplace=True,ignore_index=True)

# print(X_train.isna().sum())
# print(X_test.isna().sum())

def age(df):
    # 중앙값으로 대체
    df['Age'].replace({'1*':15,'2*':25,'3*':35,'4*':45},inplace=True)
    df['Age']=df['Age'].astype('int')
    return df

X_train=age(X_train)
X_test=age(X_test)

for col in X_train.columns:
    if X_train[col].dtype=='object':
        if len(X_train[col].value_counts())>10:
            X_train.drop(columns=col,inplace=True)
            #print(f'{col}삭제했숑')

# 삭제된 nationality와 club을 test 에서도 삭제
X_test.drop(columns=['Nationality','Club'],inplace=True)

def work_rate(df):
    df['Work_Rate'].replace(' ','') # 공백제거
    work_rates=df['Work_Rate'].str.split('/')  # 분리
    for i in df.index:
        df['Attack']=work_rates[i][0]
        df['Defend']=work_rates[i][1]
    df.drop(columns='Work_Rate',inplace=True)
    return df
    

X_train=work_rate(X_train)
X_test=work_rate(X_test)

#X_train.corr(numeric_only=True)
# 상관관계가 높은 컬럼 Relaease_Clause, Wage 중에서 하나 삭제
X_train.drop(columns=['Release_Clause'],inplace=True)
X_test.drop(columns=['Release_Clause'],inplace=True)

# 관련없는 colum 삭제
X_train.drop(columns=['Jersey_Number'],inplace=True)
X_test.drop(columns=['Jersey_Number'],inplace=True)

from sklearn.model_selection import train_test_split
X_train,X_val,y_train,y_val=train_test_split(X_train,y_train,test_size=0.2)

from sklearn.preprocessing import OneHotEncoder

category=['Preferred_Foot','Position_Class','Attack','Defend']

enc=OneHotEncoder(sparse=False).fit(X_train[category])
X_train_OH=enc.transform(X_train[category])
X_val_OH=enc.transform(X_val[category])
X_test_OH=enc.transform(X_test[category])

from sklearn.preprocessing import StandardScaler

col_conti=['Overall','Height_cm','Weight_lb','Wage']

X_train_conti=X_train[col_conti]
X_val_conti=X_val[col_conti]
X_test_conti=X_test[col_conti]

scaler=StandardScaler().fit(X_train_conti)

X_train_st=scaler.transform(X_train_conti)
X_val_st=scaler.transform(X_val_conti)
X_test_st=scaler.transform(X_test_conti)

import numpy as np

X_Train=np.concatenate([X_train_OH,X_train_st],axis=1)
X_Val=np.concatenate([X_val_OH,X_val_st],axis=1)
X_Test=np.concatenate([X_test_OH,X_test_st],axis=1)

y_Train=y_train.values.ravel()
y_Val=y_val.values.ravel()

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.metrics import mean_squared_error

# Randomforest
rf=RandomForestRegressor()
model_rf=rf.fit(X_Train,y_train)
y_pred_rf=model_rf.predict(X_Val)
mse_rf=mean_squared_error(y_pred_rf,y_Val,squared=False)
print('mse_rf',mse_rf)


# Adaboost

ada=AdaBoostRegressor()
model_ada=ada.fit(X_Train,y_Train)
y_pred_ada=model_ada.predict(X_Val)
mse_ada=mean_squared_error(y_pred_ada,y_Val,squared=False)
print('mse_ada',mse_ada)

Test=model_ada.predict(X_Test)
rr={'ID':ID,'Value':Test}
result=pd.DataFrame(rr)
result.to_csv('FIFA_X_test.csv',index=False)


