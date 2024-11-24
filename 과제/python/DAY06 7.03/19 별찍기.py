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
        # else:
        #     print(' ',end='')
    print()
