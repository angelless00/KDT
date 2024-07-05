#-----------------------------------------------------------------------------------------------
# 사용자 정의 함수
# 목적 : 매개변수의 개수를 유동적으로
#        0개~N개까지 가능하도록
# 형식 : def 함수명( *변수명 ) <= 0개~N개 데이터
#-----------------------------------------------------------------------------------------------
# 함수 기능 : N개의 정수를 덧셈 한 후 결과를 리턴 하는 함수
# 함수 이름 : add
# 매개 변수 : 0개~N개
# 함수 결과 : 덧셈 계산값 result
#-----------------------------------------------------------------------------------------------
def add(*nums):
    total=0
    for i in nums:
        total +=i
    return total

print(add(1,4,6,4,3))

