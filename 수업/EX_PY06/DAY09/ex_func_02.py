#-----------------------------------------------------------------------------------------------
# 함수(Function) 이해 및 활용
# 함수기반 계산기 프로그램
# - 4칙 연산 기능별 함수 생성 => 덧셈, 뺄셈, 곱셈, 나눗셈
# - 2개 정수만 계산 
#-----------------------------------------------------------------------------------------------

def plus(num1,num2):
    return num1+num2

def minus(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2 if num2 else '0으로 나눌수 없음'

def cross(num1,num2):
    return num1*num2

## 계산기 프로그램---------------------------------------------------------------------------------
# - 사용자가 종료를 원할 떄 종료 => 'x','X' 입력시 종료
# - 연산방식과 숫자 데이터 입력 받기
while True:
    req=input('연산(+,-,*,/)과 정수 두개를 입력(예: + 10 2) : ')
    if req=='x' or req=='X':
        print('계산기를 종료합니다.')
        break
    op,num1,num2=req.split()
    num1=int(num1)
    num2=int(num2)
    if op=='+':
        print(f'{num1}+{num2}={plus(num1,num2)}')
    elif op=='-':
        print(f'{num1}-{num2}={minus(num1,num2)}')
    elif op=='*':
        print(f'{num1}*{num2}={cross(num1,num2)}')
    elif op=='/':
        print(f'{num1}/{num2}={div(num1,num2)}')
    else:
        print('지원되지 않는 연산입니다.')










