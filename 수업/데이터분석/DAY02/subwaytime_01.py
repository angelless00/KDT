import csv

result=[]
total_number=0
with open('subwaytime.csv',encoding='utf-8-sig') as f:
    data=csv.reader(f)
    next(data)      # 두 줄의 헤더 정보를 건너뜀
    next(data)
    for row in data:
        row[4:]=map(int,row[4:])    #문자열을 숫자로 변경 후 원래 위치에 저장
        total_number+=row[4]
        result.append(row[4])   # 새벽 4시 승차인원을 result에 추가

print(f'총 지하철 역의 수: {len(result)}')
print(f'새벽 4시 승차인원: {total_number:,}')


