'''
Cars93 데이터셋에서 'Price' 컬럽은 'Min_Price' 컬럼과 'Max_Price'의 평균으로 알려져있다.
이와 같은 사실을 통해 'Price' 컬럼의 결측치의 원래의 값을 계산한 후,
'Price'가 14.7보다 작거나 25.3보다 크면서 'Large'타입인 레코드 수를 계산하여라.
'''
import pandas as pd
DF=pd.read_csv('../Cars93.csv')

#DF['Price'].fillna(DF[['Min_Price','Max_Price']].mean(axis=1))
null_cond=DF['Price'].isna()
DF['Price'][null_cond]=(DF['Min_Price'][null_cond]+DF['Max_Price'][null_cond])/2



cnt=DF[(DF['Price']<=14.7)|((DF['Price']>=25.3)&(DF['Type']=='Large'))].shape[0]
print(cnt)
