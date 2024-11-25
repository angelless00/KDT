'''
Melanoma 데이터셋을 불러와 1번쨰~122번쨰 레코드와 123번째 이후 레코드로 데이터셋을 분리하고
각 데이터셋별로 thickness 컬럼을 z-score 정규화로 변환한후
-1과 1사이의 값들의 중앙값을 각각 산출한 후 합계를 구하여라.
(단, z-score로 변환 계산에 사용되는 평균과 표준편차는 분리된 것과 관계없이 1번째 ~123번쨰 레코드로 이루어진 데이터셋을
기준으로 하고 출력시 소수점 넷쨰 자리까지 반올림하여 나타낼 것, 레코드 번호는 가장 위에 위치한 레코드를 1번으로 가정함)
'''
import pandas as pd
DF=pd.read_csv('../Melanoma.csv')
DF1=DF.iloc[:123]
DF2=DF.iloc[123:]

def normalize(sr):
    return (sr-DF1.thickness.mean())/DF1.thickness.std()

thick_normal1=normalize(DF1.thickness)
thick_normal2=normalize(DF2.thickness)

mm1=thick_normal1[(thick_normal1>-1)&(thick_normal1<=1)].median()
mm2=thick_normal2[(thick_normal2>-1)&(thick_normal2<=1)].median()

print(round((mm1+mm2),4))