#p.373 29.1.3 소스파일에서 함수를 만들고 호출하기
def hello():
    print('Hello, world!')
hello()

#p.379 29.5 함수의 호출 과정 알아보기
def mul(a,b):
    c=a*b
    return c

def add(a,b):
    c=a+b
    print(c)
    d=mul(a,b)
    print(d)

x=10
y=20
add(x,y)

#p.384 29.7 연습문제 : 몫과 나머지를 구하는 함수 만들기
x=10
y=3

def get_quotient_remainder(a,b):
    return a//b,a%b

quotient,remainder=get_quotient_remainder(x,y)
print(f'몫 : {quotient}, 나머지 : {remainder}')

#p.384 29.8 심사문제 : 사칙 연산 함수 만들기
x,y = map (int,input().split())

#219
def calc(num1,num2):
    p=num1+num2
    m=num1-num2
    d=num1/num2
    mul=num1*num2
    return p,m,mul,d

a,s,m,d=calc(x,y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a,s,m,d))







