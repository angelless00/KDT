#-------------------- ---------------------------------------------------------------------------
# => 중첩조건문
# - 조건문에 조건문이 존재하는 제어문
#  -형식
#   if 조건식:
#   ----실행코드
#   ----if 조건식:
#       ----실행코드
#-----------------------------------------------------------------------------------------------
##[실습] 숫자가 음이아닌 정수와 음수 구분하기
##       음이 아닌 정수 중에 0과 양수 구분하기
## - 음이 아닌 정수 : 숫자>=0
##  -숫자>0
#-----------------------------------------------------------------------------------------------
num=8

if num>=0:
    print(f'{num}은 음이 아닌 정수')
    if num>0:
        print(f'{num}은 양수')
    else:
        print(f'{num}은 영')
else:
    print(f'{num}은 음수')





