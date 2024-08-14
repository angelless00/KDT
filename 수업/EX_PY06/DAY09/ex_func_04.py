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

#-----------------------------------------------------------------------------------------------
# 함수기능 : 계산기 메뉴를 출력하는 함수
# 함수이름 : print_menu
# 매개변수 : 없음
# 함수결과 : 없음
#-----------------------------------------------------------------------------------------------
def print_menu():
    print(f'{"*":*^17}')
    print(f'{"계 산 기":^17}')
    print(f'{"*":*^17}')
    print(f'{"*  1. 덧    셈  *":16}')
    print(f'{"*  2. 뺄    셈  *":16}')
    print(f'{"*  3. 곱    셈  *":16}')
    print(f'{"*  4. 나 눗 셈  *":16}')
    print(f'{"*  5. 종    료  *":16}')
    print(f'{"*":*^17}')

# print(f'{"*":^16}')   16칸만들고 가운데정렬
# print(f'{"*":<16}')   16칸만들고 왼쪽정렬
# print(f'{"*":>16}')   16칸만들고 오른쪽정렬
# print(f'{"*":-^16}')   16칸만들고 빈공간 -로 채우기


#-----------------------------------------------------------------------------------------------
# 함수기능 : 연산 수행 후 결과를 반환하는 함수
# 함수이름 : clac
# 매개변수 : 함수명
# 함수결과 : 없음
#-----------------------------------------------------------------------------------------------
def calc(func,op):
    # num1,num2=input('정수 2개(예:10 2) : ').split()
    # num1=int(num1)
    # num2=int(num2)
    data=input('정수 2개(예:10 2):')
    if check_data(data,2):
        data=data.split()
        print(f'결과 :{data[0]}{op}{data[1]}={func(int(data[0]),int(data[1]))}')
    else:
        print(f'{data}는 올바른 데이터가 아닙니다.')

#-----------------------------------------------------------------------------------------------
# 함수기능 : 입력 받은 데이터가 유효한 데이터인지 검사하는 함수
# 함수이름 : check_data
# 매개변수 : str데이터(예:'10 3'), 데이터 개수
# 함수결과 : True 또는 False
#-----------------------------------------------------------------------------------------------
# def check_data(data,count):   => 내코드
#     data=data.split()
#     result=True
#     if len(data)!=count:
#         result=False
#     for i in data:
#         if i.isdecimal=False:
#             result=False
#             break
#     return result

def check_data(data,count):     #강사님코드
    data=data.split()
    if len(data)==count:
        isOk=True
        for d in data:
            if not d.isdecimal():
                isOk=False
                break
            return isOk
        else:
            return False


## 계산기 프로그램---------------------------------------------------------------------------------
# - 사용자에게 원하는 계산을 선택하는 메뉴 출력
# - 종료 메뉴 선택시 프로그램 종료
#-----------------------------------------------------------------------------------------------
while True:
    #메뉴 출력
    print_menu()

    #메뉴 션택 요청
    choice=input('메뉴 선택 : ')
    if choice.isdecimal:
        choice=int(choice)
    else:
        print("1~5사이의 숫자만 입력하세요.")
        continue

    #종료 조건(5번 메뉴 선택) 처리
    if choice==5:
        break
    elif choice==1:
        print('덧셈')
        calc(plus,'+')
    elif choice==2:
        print('뺄셈')
        calc(minus,'-')
    elif choice==3:
        print('곱셈')
        calc(cross,'*')
    elif choice==4:
        print('나눗셈')
        calc(div,'/')









