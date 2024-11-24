def rule(row,column,n,mabang,i):
    if (row==0) & (column==n-1):
        row=1
    elif row ==0:
        column=column+1
        row=n-1
    elif column==n-1:
        row=row-1
        column=0
    elif mabang[row-1][column+1]!=0:
        row=row+1
        column=column
    else:
        row=row-1
        column=column+1
        
    
    return row,column



def game(n):
    mabang=[]
    for _ in range(n):
        list_mabang=[]
        for _ in range(n):
            list_mabang.append(0)
        mabang.append(list_mabang)
    row=0
    column=int((n-1)/2)
    mabang[row][column]=1
    for i in range(2,n**2+1):
        area=rule(row,column,n,mabang,i)
        row=area[0]
        column=area[1]
        mabang[row][column]=i
    return mabang
        
n=int(input('수차 배열의 크기를 입력하세요:'))
if n%2==0:
    print('짝수를 입력하였습니다. 다시 입력하세요')
elif n%2==1:
    print(f'Magic Squrare ({n}X{n})')
    print('\n')
    mabang=game(n)
    for row in range(n):
        for column in range(n):
            print(f'{mabang[row][column]:3}',end='')
        print('\n')