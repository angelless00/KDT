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
prices.sort()
for i in prices:
    print(f'{i}') ####### 출력 어케함!?!??!?!?!