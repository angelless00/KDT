import csv

f=open('subwayfee.csv',encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)  
rate=0

for row in data:
    for i in range(4,8):
        row[i]=int(row[i])  # 4,5,6,7 컬럼값을 정수로 변환
    rate=row[4]/(row[4]+row[6])
    if row [6]==0:   # 무임승차 인원[6]이 없는 역 출력
        print(row)

f.close()