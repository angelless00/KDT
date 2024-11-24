'''
Cars93데이터셋의 Weight컬럼을 Min_Max로 정규화로 변환한후 
0.5보다 작은값들의 분산과 0.5보다 큰 값들의 분산의 차이를 구하여라.
단, 차이는 큰값에서 작은값들을 뺴서 구하며,
소수점 넷쨰자리에서 반올림하여 표현할것
'''
import pandas as pd
DF=pd.read_csv('../Cars93.csv')
weight=DF[['Weight']]



from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()
weight_scaled=scaler.fit_transform(weight)
### 스케일러엔2차원으로 넣지


low=weight_scaled[weight_scaled<0.5].var()
high=weight_scaled[weight_scaled>0.5].var()

print(abs(round(high-low,3)))

