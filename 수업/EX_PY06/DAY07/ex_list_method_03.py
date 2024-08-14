#-----------------------------------------------------------------------------------------------
# 리스트 전용의 합수 즉, 메서드(Method)
# - 리스트의 원소/요소를 제어하기 위한 함수들 
#-----------------------------------------------------------------------------------------------
# [메서드 - 요소 순서 제어 메서드 reverse()]
import random as rad

rad.seed(10)        #동일한 랜덤 숫자 추출을 위한 기준점
datas=[]
for _ in range(10):
    datas.append(rad.randint(1,30))
print(f'datas 개수 : {len(datas)},{datas}')

## 0번을 -1번으로 -1번을 0번으로 순서 뒤집기
datas.reverse()
print(f'datas 개수 : {len(datas)},{datas}')


# [메서드 - 요소 크기를 비교하여 정렳해주는 메서드 sort()]
## - 기본정렬 : 오름차순 즉, 작은 데이터부터 큰 데이터 순서로
datas.sort()
print(f'datas 개수 : {len(datas)},{datas}')

## - 내림차순 즉, 큰 데이터부터 작은 데이터 
datas.sort(reverse=True)
print(f'datas 개수 : {len(datas)},{datas}')

# [메서드 - 리스트에서 요소를 꺼내는 메서드 pop()]
## - 리스트에서 요소가 삭제됨
value=datas.pop()       # 제일 마지막 원소/요소
print(f'value : {value} 원소의 갯수 : {len(datas)}개, {datas}')

value=datas.pop(0)       # 특정 인덱스의 원소/요소
print(f'value : {value} 원소의 갯수 : {len(datas)}개, {datas}')

# [메서드 - 리스트 확장 메서드 extend()]
datas.extend([11,22,33])
print(datas)

datas.extend((55,77))
print(datas)

datas.extend({555,555,777,777})
print(datas)

datas.extend('Good Luck')
print(datas)

datas.extend({'name':'홍길동','age':12}) # ==> 키만들어감
print(datas)

# [메서드 - 모든 원소 삭제 메서드 clear()]
datas.clear()
print(f'datas 개수 : {len(datas)},{datas}')