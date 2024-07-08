Idol_list={'그룹1':[2010,'보이그룹',{'멤버':['멤버1','멤버2','멤버3']}],
           '그룹2':[2011,'걸그룹',{'멤버':['멤1','멤2','멤3']}]}

def generation(year):
    if year<=1998:
        result='1세대'
    elif year<=2002:
        result='1.5세대'
    elif year<=2008:
        result='2세대'
    elif year<=2011:
        result='2.5세대'
    elif year<=2017:
        result='3세대'
    elif year<=2019:
        result='3.5세대'
    else:
        result='4세대'
    return result    

def first_menu():
    print(f'{"-":-^21}')
    print(f'{"|    M  E  N  U     |":20}')
    print(f'{"-":-^21}')
    print(f'{"| 1.그룹명 검색     |":20}')
    print(f'{"| 2.세대별 검색     |":20}')
    print(f'{"| 3.아이돌 멤버 검색|":20}')
    print(f'{"| 4.새 아이돌 추가  |":20}')
    print(f'{"| Q.종료            |":20}')
    print(f'{"-":-^21}')
    
while True:
    first_menu()
    first_in=input('입력:')
    
    if first_in=='1':
        while True:
            find_group=input('이전으로 : B\n그룹명 입력 : ')
            if find_group=='b' or find_group=='B':
                break
            elif find_group not in Idol_list:
                print(f'{find_group}에 대한 정보가 없습니다.')
            else:
                print(f'{find_group}은 {Idol_list[find_group][0]}년도에 데뷔한 {Idol_list[find_group][1]}으로 ',end='')
                for member in Idol_list[find_group][2]['멤버']:
                    print(member,end=' ')
                print('가 소속되어있습니다.')

    elif first_in=='2':
        while True:
            second_in=input('1. 1세대\n2. 1.5세대\n3. 2세대\n4. 2.5세대\n5. 3세대\n6. 3.5세대\n7. 4세대\nB.이전으로\n입력 :')
            if second_in=='b' or second_in=='B':
                break
            elif second_in=='1':
                print('1세대 아이돌은',end=' ')
                for group_name in Idol_list:
                    if generation(Idol_list[group_name][0])=='1세대':
                        print(group_name,end=' ')
                print('가 포함되어 있습니다.')
            elif second_in=='2':
                print('1.5세대 아이돌은',end=' ')
                for group_name in Idol_list:
                    if generation(Idol_list[group_name][0])=='1.5세대':
                        print(group_name,end=' ')
                print('가 포함되어 있습니다.')
            elif second_in=='3':
                print('2세대 아이돌은',end=' ')
                for group_name in Idol_list:
                    if generation(Idol_list[group_name][0])=='2세대':
                        print(group_name,end=' ')
                print('가 포함되어 있습니다.')
            elif second_in=='4':
                print('2.5세대 아이돌은',end=' ')
                for group_name in Idol_list:
                    if generation(Idol_list[group_name][0])=='2.5세대':
                        print(group_name,end=' ')
                print('가 포함되어 있습니다.')
            elif second_in=='5':
                print('3세대 아이돌은',end=' ')
                for group_name in Idol_list:
                    if generation(Idol_list[group_name][0])=='3세대':
                        print(group_name,end=' ')
                print('가 포함되어 있습니다.')
            elif second_in=='6':
                print('3.5세대 아이돌은',end=' ')
                for group_name in Idol_list:
                    if generation(Idol_list[group_name][0])=='3.5세대':
                        print(group_name,end=' ')
                print('가 포함되어 있습니다.')
            elif second_in=='7':
                print('4세대 아이돌은',end=' ')
                for group_name in Idol_list:
                    if generation(Idol_list[group_name][0])=='4세대':
                        print(group_name,end=' ')
                print('가 포함되어 있습니다.')
            else:
                print('잘못된 입력입니다.')

    elif first_in=='3':
        while True:
            name_in=input('B. 뒤로가기\n이름 입력 : ')
            if name_in=='B' or name_in=='b':
                break
            else: 
                for idol in Idol_list:
                    for mem_name in Idol_list[idol][2]['멤버']:
                        if mem_name==name_in:
                            print(f'{name_in}은 {Idol_list[idol][0]}에 데뷔한 {idol}의 멤버입니다.')
##잘못된 입력 체크



    elif first_in=='4':
        print('입력완료')

    elif first_in=='q' or first_in=='Q':
        print('아이돌 백과사전을 종료합니다.')
        break

    else: print('잘못된 입력입니다.')























