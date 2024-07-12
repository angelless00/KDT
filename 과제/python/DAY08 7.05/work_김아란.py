#p.303 24.4 연습문제 : 파일 경로에서 파일명만 가져오기
path='C:\\KDT\\EX_PY06\\DAY04\\python.exe'
idx=path.rfind('\\')
filename=path[idx+1:]
print(filename)

#p.305 24.5 심사문제 : 특정 단어 개수 세기
text=input()
print(text.count('the '))

#p.305 24.5 심사문제 : 높은 가격순으로 출력하기
prices=list(map(int,input().split(';')))
prices.sort(reverse=True)
prices=map(str,prices)
for i in prices: 
    if len(i)>6:
        print('%3s,%3s,%3s'%(i[:-6],i[-7:-4],i[-4:-1]))
    elif len(i)>3:
        print('%3s %3s,%3s'%('',i[:-4],i[-4:-1]))
    else:
        print('%3s %3s,%3s'%('','',i[:-1]))


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

#p.397 30.6 연습문제 : 가장 높은 점수를 구하는 함수 만들기
korean,english,mathematics,science=100,86,81,91

def get_max_score(*param)
    return max(param)

max_score=get_max_score(korean,english,mathematics,science))
print('높은점수:',max_score)

max_score=get_max_score(english,science)
print('높은점수:',max_score)

#p.398 30.7 심사문제 : 가장 낮은 점수, 높은 점수와 평균점수 구하는 함수만들기

korean,english,mathematics,science=map(int,input().split())

def get_min_max_score(*parms):
    return min(parms),max(parms)

def get_average(**parms):
    return sum(parms.values())/len(parms)

min_score,max_score=get_min_max_score(korean,english,mathematics,science)
average_score=get_average(korean=korean,english=english,mathematics=mathematics,science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score,max_score,average_score))

min_score,max_score=get_min_max_score(english,science)
average_score=get_average(english=english,science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score,max_score,average_score))








