import pandas as pd 

X_train=pd.read_csv('../College_X_train.csv',encoding='cp949')
X_test=pd.read_csv('../COllege_X_test.csv',encoding='cp949')
y_train=pd.read_csv('../College_y_train.csv',encoding='cp949')

ID=X_test['ID']

X_train.drop(columns='ID',inplace=True)
X_test.drop(columns='ID',inplace=True)
y_train.drop(columns='ID',inplace=True)

# 학교명은 관련없으므로 삭제
X_train.drop(columns='Name',inplace=True)
X_test.drop(columns='Name',inplace=True)

y_train.replace({'Yes':1,'No':0},inplace=True)

# 결측치확인
#print(X_train.isna().sum())
# 없음

# 중복치확인
#print(X_train.duplicated().sum())
# 없음

# 상관관계확인
#print(X_train.corr())
# Accept가 APPs와 Enroll ,F.undergrad 와 매우 유사해서 뒤의 두 컬럼삭제
X_train.drop(columns=['Apps','Enroll','F.Undergrad'],inplace=True)
X_test.drop(columns=['Apps','Enroll','F.Undergrad'],inplace=True)

# Top10perc Top25perc 유사 하나 삭제
X_train.drop(columns='Top10perc',inplace=True)
X_test.drop(columns='Top10perc',inplace=True)

X_train.drop(columns=['Room.Board','Terminal'],inplace=True)
X_test.drop(columns=['Room.Board','Terminal'],inplace=True)
#print(X_train.corr())


# 기초통계량 확인
# print(X_train.describe())

from sklearn.model_selection import train_test_split

X_train,X_val,y_train,y_val=train_test_split(X_train,y_train,test_size=0.1,stratify=y_train)

# 스케일링

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
scaler.fit(X_train)
X_train_sc=scaler.transform(X_train)
X_val_sc=scaler.transform(X_val)
X_test_sc=scaler.transform(X_test)




y_train=y_train.values.ravel()
y_val=y_val.values.ravel()

from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier

# Ada
model_ada=AdaBoostClassifier()
model_ada.fit(X_train_sc,y_train)
pred_ada=model_ada.predict_proba(X_val_sc)[:,1]

from sklearn.metrics import roc_curve,auc

fpr,tpr,th=roc_curve(y_val,pred_ada)
score_ada=auc(fpr,tpr)
print('ada',score_ada)

# Ada
model_rf=RandomForestClassifier()
model_rf.fit(X_train_sc,y_train)
pred_rf=model_rf.predict_proba(X_val_sc)[:,1]
from sklearn.metrics import roc_curve,auc

fpr,tpr,th=roc_curve(y_val,pred_rf)
score_rf=auc(fpr,tpr)
print('rf',score_rf)


rr=model_rf.predict_proba(X_test_sc)[:,1]
# print(model_rf.predict_proba(X_test_sc))
# print(model_rf.predict(X_test_sc))
data={'ID':ID,'prob_Private':rr}
result=pd.DataFrame(data)
result.to_csv('123.csv',index=False,encoding='cp949')