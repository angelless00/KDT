'''
Cars93 데이터셋의 Max_Price 컬럼과 Min_Price컬럼에 대해서 각가 정렬한 후 정렬된 순서에 따라 
레코드 별로 Max_Price와 Min_Price의 차이를 산출하고 차이값에 대해 표준편차를 구하여라.
(단, Max_Price의 정렬은 내림차순, Min_Price의 정렬은 오름차순으로 하며,
출력시 표준편차는 소수점 넷쨰 자리에서 반올림하여 표현할것)
'''
import pandas as pd 

DF=pd.read_csv('../Cars93.csv')
min_price=DF.Min_Price.sort_values(ascending=True,ignore_index=True)
max_price=DF.Max_Price.sort_values(ascending=False,ignore_index=True)

#### ignore_index 필수!!!

diff=max_price-min_price

print(round(diff.std(),3))
