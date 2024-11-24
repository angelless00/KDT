'''
Cars93 데이터셋을 이용하여 Manufacturer,Origin컬럼의 유일값 조합의 수와
Manufacurer 컬럽의 앞 두글자만 추출한 결과와 
Origin컬럼과의 유일값 조합 수의 차이을 구하여라 
(단, 원래 유일값 조합 수에서 추출이후 수를 뺄것)
'''

import pandas as pd

DF=pd.read_csv('../Cars93.csv')
mf=DF.Manufacturer
ori=DF.Origin

DF1=DF[['Manufacturer','Origin']]
uni=DF1.drop_duplicates()
num_uniq=len(uni)

DF['mf_2']=mf.str[:2]

DF2=DF[['mf_2','Origin']]
uni_2=DF2.drop_duplicates()
num_uniq2=uni_2.shape[0]

print(num_uniq-num_uniq2)
