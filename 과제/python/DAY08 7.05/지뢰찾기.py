#p.285 23.7 심사문제 : 지뢰찾기
col,row=map(int,input().split())
matrix=[]
for i in range(row):
    matrix.append(list(input()))

new_line=[]                     #새 가로줄 생성
for j in range(col+2):
    new_line.append('.')

for i in range(row):
    matrix[i].insert(0,'.')
    matrix[i].append('.')

matrix.insert(0,new_line)
matrix.append(new_line)        #테두리 생성

for i in range(1,row+1):            #카운팅
    for j in range(1,col+1):
        if matrix[i][j]=='.':
            cnt=0
            for a in range(i-1,i+2):
                for b in range(j-1,j+2):
                    if matrix[a][b]=='*':
                        cnt=cnt+1
            matrix[i][j]=cnt

del matrix[row+1]           # 테두리 지우기
del matrix[0]

for i in range(row):
    del matrix[i][0]
    del matrix[i][col]

for i in range(row):
    for j in range(col):
        print(f'{matrix[i][j]:^3}',end='')
    print()