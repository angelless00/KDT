##-----------------------------------------------------------------------------------------------
## ==>1줄로 조건식을 축약 : 조건부표현식
##----------------------------------------------------------------------------------------------- 
## [실습] 임의의 숫자가 5의배수인지아닌지 결과를 출력하세요.
data=int(input('숫자를 입력하세요. : '))

print(f'{data}는 5의 배수가 아닙니다.') if data%5 else print(f'{data}는 5의 배수입니다.')
 
## [실습] 문자열을 입력받아서 문자열의 원소 개수를 저장
## - 단 원소 개수가 0이면 None 저장
## - (1) 입력받기 input()
## - (2) 원소/요소 갯수 파악 len()
## - (3) 원소/요소 갯수 결과 저장. 단, 0인경우 None 저장
msg=input('문자열을 입력하시오 : ')
length = len(msg) if len(msg) else None
print(f'{msg}의 길이는 {length}') 

## [실습] 연산자(4칙연산자 : +,-,*,/)와 숫자 2개 입력받기
## - 입력된 연산자에 따라 계산 결과 저장
## - 예) 입력 + 10 3        출력 13
data=input('연산자와 숫자를 2개 입력하시오. : ').split()
num1=int(data[1])
num2=int(data[2])
if data[0]=='+':
    result=num1+num2
elif data[0]=='*':
    result=num1*num2
elif data[0]=='/':
    result=num1/num2
elif data[0]=='-':
    result=num1-num2
else:
    print('잘못된 입력입니다')
print(result)
