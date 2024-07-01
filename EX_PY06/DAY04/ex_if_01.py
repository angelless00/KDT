#-------------------- ---------------------------------------------------------------------------
# 제어문 중 조건문 살펴보기
# - 조건에 만족하는 경우
#   즉, True가 되면 실행하는 코드와 실행되지 않는 코드를 결정하는 문법
#  -형식
#   if 조건식:
#   ----실행코드
#   ----실행코드
#   코드   <=조건에서 벗어남
#-----------------------------------------------------------------------------------------------
# [실습] 나이에 따른 버스 요금 출력하기
# - 0~5세 : 무료
# - 6~12세 : 500원
# - 13~19세 :1000원
# - 20~ :1700원 
#-----------------------------------------------------------------------------------------------
age=10
bus=['무료','500원','1000원','1700원']

#2개의 경우 => 5세 이하와 5세 초과
# if age<=5:
#     print(f'나이 {age}세는 버스 요금이 {bus[0]}입니다.')
# else:
#     print(f'나이 {age}세는 버스 요금이 {bus[1]}입니다.')


#4개의 경우 => 5세이하, 6세~12세, 13세~19세,20세~ 
age = int(input('나이를 입력하세요.'))
if age<=5:
    print(f'나이 {age}세는 버스 요금이 {bus[0]}입니다.')
if age>5 and age<=12:
    print(f'나이 {age}세는 버스 요금이 {bus[1]}입니다.')
if age>12 and age<=19:
    print(f'나이 {age}세는 버스 요금이 {bus[2]}입니다.')
if age>=20:
    print(f'나이 {age}세는 버스 요금이 {bus[3]}입니다.')

##-----------------------------------------------------------------------------------------------
## => 다중조건문
## -조건이 2개이상인경우
## -형식 => 조건이 True인 경우 실행코드 실행 후 나머지 조건은 검사x
#           조건이 False일 때문 아래 조건을 검사 진행 
#   if 조건1:
#   ----실행코드
#   esif 조건2:
#   ----실행코드
#        :
#   esif 조건n:
#   ----실행코드
#   else:
#   ----실행코드 
#-----------------------------------------------------------------------------------------------

if age<=5:
    print(f'나이 {age}세는 버스 요금이 {bus[0]}입니다.')
elif age>5 and age<=12:
#elif age<=12:
    print(f'나이 {age}세는 버스 요금이 {bus[1]}입니다.')
elif age>12 and age<=19:
##elif age<=19:    
    print(f'나이 {age}세는 버스 요금이 {bus[2]}입니다.')
else:
    print(f'나이 {age}세는 버스 요금이 {bus[33]}입니다.')

