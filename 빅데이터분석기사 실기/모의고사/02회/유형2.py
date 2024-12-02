import pandas as pd

X_train=pd.read_csv('BlackFriday_X_train.csv',encoding='cp949')
X_test=pd.read_csv('BlackFriday_X_test.csv',encoding='cp949')
y_train=pd.read_csv('BlackFriday_y_train.csv',encoding='cp949')

y_train=y_train.Purchase
#print(X_train)

#print(X_train.info())

# 필요없는 컬럼들 삭제
X_train.drop(columns=['User_ID','Product_ID','Product_Category_2','Product_Category_3'],inplace=True)
X_test.drop(columns=['User_ID','Product_ID','Product_Category_2','Product_Category_3'],inplace=True)

# print(X_train.info())
# print(X_test.info())

# train 테스트 둘다 2,3 결측값이 많아 삭제

#print(X_train.head(10))
#print(X_train.head())

X_train[['Occupation' ,'Marital_Status','Product_Category_1']]=X_train[['Occupation','Marital_Status','Product_Category_1']].astype('object')
X_test[['Occupation','Marital_Status','Product_Category_1']]=X_test[['Occupation','Marital_Status','Product_Category_1']].astype('object')

#print(X_train.info())


from sklearn.model_selection import train_test_split
X_train,X_val,y_train,y_val=train_test_split(X_train,y_train,test_size=0.2,random_state=69)


from sklearn.preprocessing import OneHotEncoder

encoder=OneHotEncoder(sparse=False)
encoder.fit(X_train)
X_train_OH=encoder.transform(X_train)
X_val_OH=encoder.transform(X_val)
X_test_OH=encoder.transform(X_test)

from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.metrics import mean_absolute_error
# rf
rf_model=RandomForestRegressor(n_estimators=200)
rf_model.fit(X_train_OH,y_train)
rf_pred=rf_model.predict(X_val_OH)
rf_score=mean_absolute_error(y_val,rf_pred)
print('rf',rf_score)


# # ada
# ada_model=AdaBoostRegressor(n_estimators=100)
# ada_model.fit(X_train_OH,y_train)
# ada_pred=ada_model.predict(X_val_OH)
# ada_score=mean_absolute_error(y_val,ada_pred)
# print('rf',ada_score)

rr=rf_model.predict(X_test_OH)
result=pd.DataFrame(rr,columns=['Purchase'])
result.to_csv('result.csv',index=False,encoding='cp949')