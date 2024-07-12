# p.198 17.1.3 입력한 횟수대로 반복하기
count=int(input('반복할 횟수를 입력하세요: '))
i=
while i<count:
    print('Hello, world!',i)
    i=i+1

count= int(input('반복할 횟수를 입력하세요: '))
while count>0:
    print('Hello, world!',count)
    count=count-1

# p.198 17.2 반복 횟수가 정해지지 않은 경우
import random
i=0
while i!=3:
    i=random.randint(1,6)
    print(i                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  )

# 17.5 연습문제 : 변수 두개를 다르게 반복하기
i=2
j=5

while i<=32 or j>=1:
    print(i,j)
    i=i*2
    j=j-1

# p.203 17.6 심사문제 : 교통카드 잔액 출력하기
cash=int(input())
while cash>=1350:
    cash=cash-1350
    print(cash)

# p.204 18.1.1 while에서 break로 반복문 끝내기
i=0
while True:
    print(i)
    i=i+1
    if i == 100:
        break

# p.205 18.1.2 for에서 break로 반복문 끝내기
for i in range(10000):
    print(i)
    if i==100:
        break

# p.206 18.2.1 for에서 continue로 코드 실행 건너뛰기
for i in range(100):
    if i%2==0:
        continue
    print(i)

# p.207 18.2.2 while반복문에서 continue로 코드 실행 건너뛰기
i=0
while i<100:
    i=i+1
    if i % 2==0:
        continue
    print(i)

# p.208 18.3 입력한 횟수대로 반복하기
count=int(input('반복할 횟수를 입력하세요: '))

i=0
while True:
    print(i)
    i=i+1
    if i==count:
        break

# p.209 18.3.1 입력한 숫자까지 홀수 출력하기
count=int(input('반복할 횟수를 입력하세요: '))

for i in range(count+1):
    if i%2==0:
        continue
    print(i)

# p.211 18.5 연습문제: 3으로 끝나는 숫자만 출력하기
i=0
while True:
    if i%10==3:
        print(i, end=' ')
        i=i+1
    if i>73:
        break  
    i+=1          

## 더깔끔한 추가 코드 >_<
i=-1
while True:
    if i>72:
        break  
    i+=1    
    if i%10==3:
        print(i, end=' ')
      
      


# p.212 18.6 심사문제 : 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
start,stop=map(int,input().split())

i=start

while True:
    if i%10!=3:
        i=i+1
        continue
    if i>stop: 
        break
    print(i,end=' ')
    i+=1


# p.213 19.1 중첩 루프 사용하기
for i in range(5):
    for j in range(5):
        print('j:',j,sep='',end=' ')
    print('i :',i,'\\n',sep='')

# p.214 19.2 사각형으로 별 출력하기
for i in range(5):
    for j in range(5):
        print('*',end='')
    print()

# p.215 19.2.1 사각형 모양 바꾸기
for i in range(3):
    for j in range(7):
        print('*',end='')
    print()

# p.216 19.3 계단식으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j<=i:
            print('*',end='')
    print()

# p.216 19.3.1 대각선으로 별 출력하기
for i in range(5):
    for j in range(5):
        if i==j:
            print('*',end='')
        else:
            print(' ',end='')
    print()

# p.218 19.5 연습문제 : 역삼각형 모양으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j<i:
            print(' ',end='')
        else:
            print('*',end='')
    print()

# p.219 19.6 심사문제 : 산 모양으로 별 출력하기
num=int(input())
for i in range(num):
    for j in range(2*num):
        if j<num-i:
            print(' ',end='')
        elif num-i<=j<=num+i:
            print('*',end='')
        else:
            print(' ',end='')
    print()

# p.221 20.3 3과 5의 공배수 처리하기 
for i in range(1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

# p.223 코드 단축하기
for i in range(1,101):
    print('Fizz'*(i%3==0)+'Buzz'*(i%5==0)or i)

# p.225 20.7 연습문제 : 2와 11의 배수, 공배수 처리하기
for i in range(1,101):
    if i%2==0 and i%11:
        print('FizzBuzz')
    elif i%2==0:
        print('Fizz')
    elif i%11==0:
        print('Buzz')
    else:
        print(i)

# p.226 20.8 심사문제 : 5와 7의 배수, 공배수 처리하기
n1,n2=map(int,input().split())
for i in range(n1,n2+1):
    if i%5==0 and i%7==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Fizz')
    elif i%7==0:
        print('Buzz')
    else:
        print(i)


                                                                                      
                                     









