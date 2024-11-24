'''
Cars93 데이터셋을 이용하여 RPM컬럽의 결측치를 평균으로 대체하고 
RPM과 Wheelbase컬럽을 각각 z-점수로 표준화한후
표준화된 Whellbase에 상수 -36을 곱한 값과 표준화된 RPM컬럽의 차이값을 구하고
표준편차를 산술하여라
(단, 소수점 셋쨰자리까지 반올림하여 표현할것)
'''

import pandas as pd

DF=pd.read_csv('../Cars93.csv')
#print(DF['RPM'].isna().sum())
DF['RPM'].fillna(DF['RPM'].mean(),inplace=True)

def normalize(sr):
    return (sr-sr.mean())/sr.std()

rpm_normal=normalize(DF.RPM)
wb_normal=normalize(DF.Wheelbase)

diff=wb_normal*(-36)-rpm_normal
print(round(diff.std(),3))