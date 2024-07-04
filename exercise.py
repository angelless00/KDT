# p.219 19.6 심사문제 : 산 모양으로 별 출력하기
num=int(input())
for i in range(num):
    for j in range(2*num):
        if j<num-i:
            print(' ',end='')
        elif num-i<=j<=num+i:
            print('*',end='')
    print()
