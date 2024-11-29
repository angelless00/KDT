import pandas as pd 

X_train=pd.read_csv('../weatherAUS_X_train.csv',encoding='cp949')
X_test=pd.read_csv('../weatherAUS_X_test.csv',encoding='cp949')
y_train=pd.read_csv('../weatherAUS_y_train.csv',encoding='cp949')

#print(X_train.info()) 
# 결측치 다수 존재

#print(X_train.head())

Date=X_test['Date']

# Date는 필요하지 않으므로 삭제
y_train.drop(columns=['Date'],inplace=True)
y_train.replace({'Yes':1,'No':0},inplace=True)
#print(X_train.isna().sum())

# 결측치가 많은 cloud 컬럼 삭제
X_train.drop(columns=['Cloud9am','Cloud3pm'],inplace=True)
X_test.drop(columns=['Cloud9am','Cloud3pm'],inplace=True)

#print(X_train.isna().sum())

#print(X_train['Location'].value_counts())

# Date,Location 컬럼삭제
X_train.drop(columns=['Date','Location'],inplace=True)
X_test.drop(columns=['Date','Location'],inplace=True)

#print(X_train.corr(numeric_only=True))

# 관련성이 높은 컬럼들 삭제
X_train.drop(columns=['Temp9am','Temp3pm'],inplace=True)
X_test.drop(columns=['Temp9am','Temp3pm'],inplace=True)

X_train.drop(columns=['Pressure3pm'],inplace=True)
X_test.drop(columns=['Pressure3pm'],inplace=True)

#print(X_train.corr(numeric_only=True))

X_train['RainToday'].replace({'Yes':1,'No':0},inplace=True)
X_test['RainToday'].replace({'Yes':1,'No':0},inplace=True)

#print(X_train.head())

# 바람방향 삭제
X_train.drop(columns=['WindGustDir','WindDir9am','WindDir3pm'],inplace=True)
X_test.drop(columns=['WindGustDir','WindDir9am','WindDir3pm'],inplace=True)

#print(X_train.head())

#print(X_train.isna().sum())

X_train.dropna(inplace=True)
y_train=y_train.iloc[X_train.index]

X_test.ffill(inplace=True)


# 데이터셋 분리
from sklearn.model_selection import train_test_split
X_train,X_val,y_train,y_val=train_test_split(X_train,y_train,test_size=0.2)

# 스케일링

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
scaler.fit(X_train)
X_Train=scaler.transform(X_train)
X_Val=scaler.transform(X_val)
X_Test=scaler.transform(X_test)

from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.metrics import roc_curve,auc

## ada
model_ada=AdaBoostClassifier()
model_ada.fit(X_Train,y_train)
pred_ada=model_ada.predict_proba(X_Val)[:,1]
fpr,tpr,th=roc_curve(y_val,pred_ada)
ada_score=auc(fpr,tpr)
print('ada',ada_score)

## Random
model_rf=RandomForestClassifier()
model_rf.fit(X_Train,y_train)
pred_rf=model_rf.predict_proba(X_Val)[:,1]
fpr,tpr,th=roc_curve(y_val,pred_ada)
rf_score=auc(fpr,tpr)
print('rf',rf_score)

# 바람방향 삭제시 둘다 비슷하기 0.78정도의 성능

rr=model_rf.predict_proba(X_Test)[:,1]
data={'Date':Date,'RainTomorrow_Prob':rr}
result=pd.DataFrame(data)
result.to_csv('1234.csv',encoding='cp949',index=False)





