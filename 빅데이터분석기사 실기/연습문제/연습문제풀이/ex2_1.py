"""
Q. Cars93 데이터셋의 Wheelbase 컬럼에 대해서 평균 값에서 표준편차의 1.5배 2배 2.5배를 더하거나 뺀 값들의 
구간 내의 데이터들의 평균을 각각 구한 후 원래의 데이터 평균에서 뺏을 떄 차이들의 합을 출력하여라. 
(단, 소수점 다섯쨰 자리에서 반올림하여 표현할것)
"""

import pandas as pd

df=pd.read_csv('../Cars93.csv')
#print(df)

WB=df.Wheelbase
WB_mean=WB.mean()
WB_std=WB.std()

# 1.5
low_1=WB_mean-1.5*WB_std
high_1=WB_mean+1.5*WB_std

# 2
low_2=WB_mean-2*WB_std
high_2=WB_mean+2*WB_std

# 2.5
low_3=WB_mean-2.5*WB_std
high_3=WB_mean+2.5*WB_std


avg1=WB[(low_1<=WB)&(WB<=high_1)].mean()
avg2=WB[(low_2<=WB)&(WB<=high_2)].mean()
avg3=WB[(low_3<=WB)&(WB<=high_3)].mean()

case1=WB_mean-avg1
case2=WB_mean-avg2
case3=WB_mean-avg3

print(round(case1+case2+case3,4))