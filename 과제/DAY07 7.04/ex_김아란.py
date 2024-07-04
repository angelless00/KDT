#p.270 22.9 연습문제: 리스트에서 특정 요소만 뽑아내기
a=['alpha','bravo','chalie','delta','echo','foxtrot','golf','hotel','india']
b=[msg for msg in a  if len(msg)==5]
print(b)

#p.271 22.10 심사문제 : 2의 거듭제곱 리스트 생성하기
start,end=map(int,input().split())
data=list(range(start,end+1))
data.pop(1)
data.pop(-2)

result=[2**num for num in data]
print(result)



