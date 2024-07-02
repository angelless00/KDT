# P.193 16.5 연습문제 : 리스트의 요소에 10을 곱해서 출력하기
x=[49,-17,25,102,8,62,21]
for i in x:
    print(i*10,end=' ')

# p.193 16.6 심사문제 : 구구단 출력하기
gugudan=int(input())
for i in range(1,10):
    print(f'{gugudan} * {i} = {gugudan*i}')