#p.275 23.2.2 for 반복문을 두번 사용하기
a=[[10,20],[30,40],[50,60]]

for i in a:
    for j in i:
        print(j,end=' ')
    print()

#276 23.2.3 for와 range 사용하기
a=[[10,20],[30,40],[50,60]]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=' ')
    print()

#p.277 23.2.4 while 반복문을 한 번 사용하기
a=[[10,20],[30,40],[50,60]]

i=0
while i<len(a):
    x,y=a[i]
    print(x,y)
    i=i+1

#p.277 23.2.5 while 반복문을 두번 사용하기
a=[[10,20],[30,40],[50,60]]

i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j],end=' ')
        j=j+1
    print()
    i=i+1 

#p.278 23.3.1 for 반복문으로 1차원 리스트 만들기
a=[]
for i in range(10):
    a.append(0)
print(a)

#p.278 23.3.2 for 반복문으로 2차원 리스트 만들기
a=[]

for i in range(3):
    line=[]
    for j in range(2):
        line.append(0)
    a.append(line)
print(a)

#p.280 23.3.4 톱니형 리스트 만들기
a=[3,1,3,2,5]
b=[]

for i in a:
    line=[]
    for j in range(i):
        line.append(0)
    b.append(line)

print(b)

#p.284 23.6 연습문제 :3차원 리스트 만들기
a=[[[0 for _ in range(3)] for _ in range(4)] for _ in range(2)]
print(a)














