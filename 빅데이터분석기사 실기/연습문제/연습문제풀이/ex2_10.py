'''
Cars93 데이터셋에서 'Make'컬럼을 이용하여 제조사가 'Chevrolet','Pontian','Hyundai'이면서
'AirBags'이 'Driver'에만 있는 경우의 레코드 수를 계산하여라.
'''

import pandas as pd
DF=pd.read_csv('../Cars93.csv')
cond1=DF[(DF['Make'].str.startswith(('Chevrolet','Pontiac','Hyundai')))&(DF['AirBags']=='Driver only')]

# startswith!!! 


print(cond1.shape[0])
