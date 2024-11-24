'''
Cars93 데이터셋을 이용하여 컬럼 Type, Man_trans_avail에 대한 그룹별 RPM레코드 수와 RPM합계, 중앙값을 모두 구한 후,
그룹별 중앙값에서 그룹별 합계에서 레코드 수를 나눈 값들을 뺴서 나온 결과의 총 원소 합을 구하여라.
(단, 출력시 소수점은 첫쟤자리에서 반올림하여 표현 할 것)
'''
import pandas as pd

DF=pd.read_csv('../Cars93.csv')

GR=DF.groupby(['Type','Man_trans_avail'])['RPM']
cnt=GR.count()
ss=GR.sum()
mm=GR.median()

print(round(sum(mm-ss/cnt),0))