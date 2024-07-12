# for문 하나로 구구단 짜기

for i in range(20,100):
    a=i//10
    b=i%10
    if b==0:
        print(f'{a}단')
    else:
        print(f'{a}*{b}={a*b}')



# 구구단 가로로 뽑기

for i in range(10):
    for j in range(2,6):
        if i==0:
            print(f'{j:^4}단',end='  ')
        else:
            print(f'{j}*{i}={j*i:2}',end='  ')
    print()
for i in range(10):
    for j in range(6,10):
        if i==0:
            print(f'{j:^4}단',end='  ')
        else:
            print(f'{j}*{i}={j*i:2}',end='  ')
    print()
    


