'''
Rabbit 데이터셋을 불러와 Dose컬럼의 제3사분위수와 제2사분위수를 구하고
두 값은 차이의 절댓값을 구한수 소수점을 버린 값을 출력하여라.
'''

import pandas as pd
import numpy as np

DF=pd.read_csv('../Rabbit.csv')
dose3=DF['Dose'].quantile(0.75)
dose2=DF['Dose'].quantile(0.5)

print(int(abs(dose3-dose2)))