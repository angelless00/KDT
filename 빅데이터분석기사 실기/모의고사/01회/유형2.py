import pandas as pd

X_train=pd.read_csv('titanic3_X_train.csv',encoding='cp949')
X_test=pd.read_csv('titanic3_X_test.csv',encoding='cp949')
y_train=pd.read_csv('titanic3_y_train.csv',encoding='cp949')
ID=X_test.ID
y_train.drop(columns='ID',inplace=True)

X_train.drop(columns=['cabin','ID','name','ticket','age','embarked'],inplace=True)
X_test.drop(columns=['cabin','ID','name','ticket','age','embarked'],inplace=True)


X_train['fare'].fillna(X_train.fare.mean(),inplace=True)


#print(X_train.value_counts())

X_train['sex'].replace({'F':'female'},inplace=True)
X_test['sex'].replace({'F':'female'},inplace=True)

# print(X_train.info())

X_train['pclass']=X_train['pclass'].astype('object')
X_test['pclass']=X_test['pclass'].astype('object')

#print(X_train.info())

from sklearn.model_selection import train_test_split
X_train,X_val,y_train,y_val=train_test_split(X_train,y_train,test_size=0.1)

#print(X_train.head(10))

from sklearn.preprocessing import OneHotEncoder
ob_col=['pclass','sex']
OH_encoder=OneHotEncoder(sparse=False).fit(X_train[ob_col])

X_train_oh=OH_encoder.transform(X_train[ob_col])
X_val_oh=OH_encoder.transform(X_val[ob_col])
X_test_oh=OH_encoder.transform(X_test[ob_col])

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
num_col=['sibsp','parch','fare']
scaler.fit(X_train[num_col])
X_train_sc=scaler.transform(X_train[num_col])
X_val_sc=scaler.transform(X_val[num_col])
X_test_sc=scaler.transform(X_test[num_col])

import numpy as np
X_Train=np.concatenate([X_train_oh,X_train_sc],axis=1)
X_Val=np.concatenate([X_val_oh,X_val_sc],axis=1)
X_Test=np.concatenate([X_test_oh,X_test_sc],axis=1)

from sklearn.ensemble import AdaBoostClassifier,RandomForestClassifier
from sklearn.metrics import f1_score
# ada
ada_model=AdaBoostClassifier()
ada_model.fit(X_Train,y_train)
pred_ada=ada_model.predict(X_Val)
ada_score=f1_score(y_val,pred_ada)
print('ada',ada_score)

# rf
# rf_model=RandomForestClassifier()
# rf_model.fit(X_Train,y_train)
# pred_rf=rf_model.predict(X_Val)
# rf_score=f1_score(y_val,pred_rf)
# print('rf',rf_score)

pred=ada_model.predict(X_Test)
data={'ID':ID,'survived':pred}
result=pd.DataFrame(data)
result.to_csv('result.csv',encoding='cp949')