"""
Q.Cars93 데이터셋의 Length컬럼에 대해서 순위를 부여한 후,
1위부터 30위까지의 값들의 표준편차를 구하고
소수점 셋쨰짜리까지 반올림하여 나타내어라
(단, 동점은 동일한 순위를 부여하되 평균내서 등수를 산정하여 최솟값을 1위로함.)
"""

import pandas as pd

DF=pd.read_csv('../Cars93.csv')
Leng=DF.Length
#print(Leng)

best=Leng.rank(method='average')
best30=best[best<=30]
print(round(Leng[best30.index].std(),3))