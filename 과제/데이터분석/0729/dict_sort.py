def menu():
    print('-'*40)
    print('1. 전체 데이터 출력')
    print('2. 수도 이름 오름차순 출력')
    print('3. 모든 도시의 인구수 내림차순 출력')
    print('4. 특정 도시의 정보 출력')
    print('5. 대륙별 인구수 계산 및 출력')
    print('6. 프로그램 종료')
    print('-'*40)

def code1(table):
    num=1
    for i in table:
        print(f'[{num}] {i}: {table[i]}')
        num+=1

def code2(table):
    table_value=sorted(table)
    num=1
    for i in table_value:
        print(f'[{num}] {i:15} : {table[i][0]:15} {table[i][1]:15} {table[i][2]:15,}')
        num+=1


def code3(table):
    table_value=sorted(Table,reverse=True,key=lambda x:Table.get(x)[2])
    num=1
    for i in table_value:
        print(f'[{num}] {i:15}: {table[i][2]:15,}')
        num+=1


def code4(table):
    inp_key=input('출력할 도시 이름을 입력하세요: ')
    if inp_key in table:
        print(f'국가:{table[inp_key][0]}, 대륙:{table[inp_key][1]}, 인구수:{table[inp_key][2]:,}')
    else:
        print(table.get(inp_key,f'{inp_key}은 key에 없습니다.'))


def code5(table):
    inp_con=input('대륙 이름을 입력하세요(Asia, Europe, America): ')
    count=0
    for i in table:
        if table[i][1]==inp_con:
            count+=table[i][2]
            print(f'{i}: {table[i][2]:,}')
    print(f'{inp_con} 전체 인구수 : {count:,}')



Table={'Seoul':['South Korea','Asia',9655000],
       'Tokyo':['Japan','Asia',14110000],
       'Beijing':['China','Asia',21540000],
       'London':['United Kingdom','Europe',14800000],
       'Berlin':['Germany','Europe',3426000],
       'Mexico City':['Mexico','America',21200000]}

inp_num=0
while True:
    menu()
    inp_num=int(input('메뉴를 입력하세요: '))
    if inp_num==1:
        code1(Table)
    elif inp_num==2:
        code2(Table)
    elif inp_num==3:
        code3(Table)
    elif inp_num==4:
        code4(Table)
    elif inp_num==5:
        code5(Table)
    elif inp_num==6:
        print('프로그램을 종료합니다.')
        break









