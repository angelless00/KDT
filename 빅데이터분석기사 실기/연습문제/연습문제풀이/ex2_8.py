'''
Cars93 데이터셋을이용하여 먼저, Price컬럼의 결측치를 평균으로 대체하고
Max_Price변수와 Min_Price의 평균보다 작은 레코드만을 추출해 산출된 Origin그룹별 Price의 합계를 구하고
다음으로 Price컬럼의 결측치를 중앙값으로 대체하고,
Price컬럼이 Min_Price컬럼의 제 3분위수보다 작은 레코드만을 추출해 산출된 Origin별 Price의합계를
Origin그룹별로 합한 후 큰값을 출력하여라.
(단, 소수점이하는 모두 절삭하여 정수로 표현할 것)
'''
import numpy as np
import pandas as pd
DF= pd.read_csv('../Cars93.csv')
DF1=DF.copy()
DF2=DF.copy()

# 평균대체
DF1['Price'].fillna(DF1.Price.mean(),inplace=True)

mean1=DF1[['Max_Price','Min_Price']].mean(axis=1)
DD=DF1[DF1['Price']<mean1]
case1=DD.groupby('Origin')['Price'].sum()
print(np.floor(case1))

# 중앙값 대체
DF2['Price'].fillna(DF2['Price'].median(),inplace=True)
num3=DF2['Min_Price'].quantile(0.75)
DD2=DF2[DF2['Price']<num3]
case2=DD2.groupby('Origin')['Price'].sum()
print(np.floor(case2))

print(np.floor(case1+case2).max())