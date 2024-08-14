#-----------------------------------------------------------------------------------------------
# 사용자 정의 함수
#-----------------------------------------------------------------------------------------------
# 덧셈, 뺼셈, 곱셈, 나눗셈 함수를 각각 만들기
# - 매개변수 : 정수2개, num1, num2
# - 함수 결과 : 연산 결과 반환 
#-----------------------------------------------------------------------------------------------
def plus(num1,num2):
    return num1+num2

def minus(num1,num2):
    return num1-num2

def division(num1,num2):
    return num1/num2 if num2 else '0으로 나눌수 없음'

def cross(num1,num2):
    return num1*num2

#-----------------------------------------------------------------------------------------------
# 함수 기능 : 입력 데이터가 유효한 데이터인지 검사해주는 기능
# 함수 이름 : check_data
# 매개 변수 : 문자열 데이터, 데이터 갯수 data, count,sep=''
# 함수 결과 : 유효여부 True/False 
#-----------------------------------------------------------------------------------------------
def check_data(data,count,sep=' '):
# 데이터여부
    if len(data):
#데이터 분리후 갯수 체크
        data2=data.split(sep)
        return True if count==len(data2) else False

    
print(check_data('= 2 4',3))
print(check_data('= 4',3))

## [실습] 사용자로부터 연산자, 숫자1, 숫자2를 입력받아서 연산결과를 출력해주세요.
# - input("연산자, 숫자1, 숫자2 : ").split(',')
mark,num1,num2=input("연산자 숫자1 숫자2 : ").split()
num1=int(num1)
num2=int(num2)
if mark not in ['+','-','/','*']:
    print('잘못된 연산자 입니다.')
else:
    if mark=='+':
        print(plus(num1,num2))
    elif mark=='-':
        print(minus(num1,num2))
    elif mark=='*':
        print(cross(num1,num2))
    elif mark=='/':
        print(division(num1,num2))
    else:
        print('잘못된 입력입니다.')