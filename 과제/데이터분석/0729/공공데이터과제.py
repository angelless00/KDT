import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

dataDF=pd.read_csv('subwaytime.csv',header=[0,1])

#print(dataDF.head())
#print(dataDF.columns)

subway_out=dataDF[['호선명','지하철역']]
subway_out['people_count']=0

for row in dataDF.index:
    count=0
    for col in dataDF.columns[[11,13]]:
        count+=dataDF.loc[row,col]
    subway_out.loc[row,'people_count']=int(count)

line=[]
line_max_name=[]
line_max_number=[]

for i in range(7):
    max_name=''
    max_number=0
    nline=subway_out[subway_out[('호선명','Unnamed: 1_level_1')]==str(i+1)+'호선']
    for row in range(len(nline.index)):
        if nline.iloc[row,2]>max_number:
            max_number=nline.iloc[row,2]
            max_name=nline.iloc[row,1]
    print(f'출근 시간대 {i+1}호선 최대 하차역: {max_name}, 하차인원: {max_number:,}명')
    line.append(str(i+1)+'호선 '+max_name)
    line_max_name.append(max_name)
    line_max_number.append(max_number)

plt.bar(line,line_max_number)
plt.xticks(rotation=80)
plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역')
plt.tight_layout()
plt.show()







