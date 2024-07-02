#-----------------------------------------------------------------------------------------------
# [실습1] 글자를 입력 받습니다.
#         입력 받은 글자(a~z,A~z)의 코드값을 출력합니다.
#-----------------------------------------------------------------------------------------------

char=input('글자 입력(a~z,A~z) : ')
if len(char)==1:
    if 'a'<=char<='z' or 'A'<=char<='Z':
        print(f' data {char}의 코드값 : {ord(char)}')
    else:
        print('알파벳만 가능합니다.')
else:
    print(f'한개의 알파벳 문자만 입력하시오.\n입력된 데이터를 확인하세요.')



#-----------------------------------------------------------------------------------------------
# [실습1-1] 문자가 여러개 일 떄
#-----------------------------------------------------------------------------------------------
char2='sdfupsdf'
print(list(map(ord,char2)))


#-----------------------------------------------------------------------------------------------
# [실습2] 점수를 입력 받은 후 학점을 출력합니다.
# - 학점 : A+, A, A-, B+, B, B-, C+, C, C-, D+, D ,D-, F
# A+ : 96~100
# A : 95 
# A- : 90~94  
#-----------------------------------------------------------------------------------------------
grade=int(input('점수를 입력하시오.'))
if grade<0 or grade>100:
    print("잘못입력된 점수입니다.")
else:
    if 96<=grade<=100:
        print(f'점수{grade}는 A+학점입니다.')
    elif grade==95:
        print(f'점수{grade}는 A학점입니다.')
    elif 90<=grade<=94:
        print(f'점수{grade}는 A-학점입니다.')
    elif 86<=grade<=99:
        print(f'점수{grade}는 B+학점입니다.')
    elif grade==85:
        print(f'점수{grade}는 B학점입니다.')
    elif 80<=grade<=84:
        print(f'점수{grade}는 B-학점입니다.')
    elif 76<=grade<=79:
        print(f'점수{grade}는 C+학점입니다.')
    elif grade==75:
        print(f'점수{grade}는 C학점입니다.')
    elif 70<=grade<=74:
        print(f'점수{grade}는 C-학점입니다.')
    elif 66<=grade<=69:
        print(f'점수{grade}는 D+학점입니다.')
    elif grade==65:
        print(f'점수{grade}는 D학점입니다.')
    elif 60<=grade<=69:
        print(f'점수{grade}는 D-학점입니다.')
    else:
        print(f'점수 {grade}는 F학점입니다.')  
