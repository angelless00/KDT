'''
Boston 데이터셋을 불러와 medv컬럼에서 대해서 동일한 폭으로 binning한 후 가장 많은 빈도를 가지는 구간을 산출하고
해당 구간 내 dis 컬럼의 중앙값을 구하여라.
(폭운은 10을 기준으로 하고 소수점을 둘째자리까지 나타내시오.)
'''

import pandas as pd

DF=pd.read_csv('../Boston.csv')
#print(DF['medv'].min(),DF['medv'].max())

medv_cut=pd.cut(DF['medv'],bins=[0,10,20,30,40,50])
va=medv_cut.value_counts()
max_cut=va.index[0]
print(round(DF['dis'][medv_cut==max_cut].median(),2))