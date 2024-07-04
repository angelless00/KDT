#-----------------------------------------------------------------------------------------------
# 리스트 전용의 합수 즉, 메서드(Method)
# - 리스트의 원소/요소를 제어하기 위한 함수들 
#-----------------------------------------------------------------------------------------------
import random as rad

# [1] 실습 데이터 => 임의의 정수 숫자 10개로 구성된 리스트
datas=[1,34,5,3,6,82,5,5,6,9]

# [메서드 - 요소 인덱스를 반환하는 메서드 index()]
idx=datas.index(34)
print(f'34의 인덱스 : {idx}')

if 0 in datas:
    idx=datas.index(0)
    print(f'0의 인덱스 : {idx}')
else:
    print('0은 존재하지 않는 데이터 입니다.')

# -> 5의 인덱스 찾기
   # ===> 5가 여러개인경우 첫번째만 찾고 종료! 

if 5 in datas:
    idx=datas.index(5,4)  # ===> 4번째 수 부터 검색해서 5를 찾아줘!
    print(f'5의 인덱스 : {idx}')

if 5 in datas:
    idx=datas.index(5)              # 첫번째 5를 찾아줘
    print(f'5의 인덱스 : {idx}')
    
    idx=datas.index(3,idx+1)        # 그 다음 5를 찾아줘
    print(f'5의 인덱스 : {idx}')

# [메서드 - 데이터가 몇개 존재하는 갯수를 파악하는 메서드 count(데이터)]
cnt=datas.count(5)
print(f'5의 개수 : {cnt}개')
idx=0
for i in range(cnt):
    idx=datas.index(5,idx if not i else idx+1)
    print(f'{i+1}번쨰 5의 인덱스 : {idx}')









