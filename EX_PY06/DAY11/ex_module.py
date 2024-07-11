#-----------------------------------------------------------------------------------------------
# 모듈 - 파이썬 파일(py) 1개
# - 구성 : 변수, 함수, 클래스가 존재
# -       반드시 모두다 있을 필요는 x
# - 종류 : 내장모듈 / 사용자정의모듈 /써드파티션모듈(설치필수) 
#-----------------------------------------------------------------------------------------------
# 사용법 => 현재 파이썬 파일에 포함시켜아 사용 가능함
import math
import random as rad    #모듈명이 길 경우 줄여서 별칭 지정 후 사용

## 모듈 내의 변수, 함수, 클래스 사용방법
##             :모듈명.변수명,    모듈명,함수(),  모둘명.클래스명
print(f'내장 모듈 math 안에 있는 pi변수 : {math.pi}')

print(f'내장모듈 math안에 있는 factorial()함수 : {math.factorial(3)}')

print(f'내장모듈 radnom안에 있는 random()함수 : {rad.random()}')

## 모듈명을 별칭 지정시 이전 모듈명 사용 x
## random.randnt()


