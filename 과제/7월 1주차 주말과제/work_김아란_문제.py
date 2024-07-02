# 081 별 표현식
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,_,_=scores
print(valid_score)

# 082
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,_,*valid_score=scores
print(valid_score)

# 083
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,*valid_score,_=scores
print(valid_score)

# 084 비어있는 딕셔너리
temp={}

# 085 
icecream={'메로나':1000,'폴라포':1200,'빵빠레':1800}

# 086
icecream['죠스바']=1200
icecream['월드콘']=1500
print(icecream)

# 087
print(f'메로나 가격 : {icecream["메로나"]}')

# 088
icecream['메로나']=1300

# 089
del icecream['메로나']
print(icecream)

# 090
# 없는 키를 불러냄

# 091 딕셔너리 생성
inventory={'메로나':(300,20),'비비빅':(400,3),'죠스바':(250,1000)}

# 092 딕셔너리 인덱싱
print(f'{inventory["메로나"][0]}원')

# 093 딕셔너리 인덱싱
print(f'{inventory["메로나"][1]}개')

# 094 딕셔너리 추가
inventory["월드콘"] =(500,7)
print(inventory)

# 095 딕셔너리 keys() 메서드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice=icecream.keys()
print(list(icecream))

# 096 딕셔너리 values() 메서드
price=icecream.values()
print(list(price))

# 097 딕셔너리 values() 메서드
price=list(icecream.values())
print(sum(price))

# 098 딕셔너리 update 메서드
new_product={'팥빙수':2700,'아맛나':1000}
icecream.update(new_product)
print(icecream)

# 099 zip과 dict
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result=dict(zip(keys,vals))
print(result)

# 100 zip과 dict
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table=dict(zip(date,close_price))
print(close_table)

# 101 
# bool 타입

# 102
# False

# 103
# True

# 104
# True

# 105
# True

# 106
# >=로 써야함

# 107
# 

# 108
# Hi, there.

# 109
# 1
# 2
# 4

# 110
# 3
# 5

# 111
msg=input()
print(msg*2)

# 112
num=int(input('숫자를 입력하세요: '))
print(num+10)

# 113
num=int(input())
if num%2:
    print('홀수')
else:
    print('짝수')

# 114
inp=int(input('입력값: '))
print(f'출력값: {inp+10}')

# 115
inp=int(input('입력값: '))
sol=inp-20
if sol>=0:
    print(f'출력값: {sol}')
else:
    print(f'출력값: {0}')

# 116
time=input('현재시간:')
if time[-2:]=='00':
    print('정각 입니다.')
else:
    print('정각이 아닙니다.')

# 117
fruit = ["사과", "포도", "홍시"]
fav=input("좋아하는 과일은?")
if fav in fruit:
    print('정답입니다.')
else:
    print('오답입니다.')

# 118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
inp=input("종목명 : ")
if inp in warn_investment_list:
    print('투자 경고 종목입니다.')
else:
    print('투자 경고 종목이 아닙니다.')

# 119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
season=input("제가좋아하는계절은: ")
if season in fruit:
    print('정답입니다.')
else:
    print('오답입니다.')

# 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
fr=list(fruit.values())
fav=input('좋아하는과일은?')
if fav in fr:
    print('정답입니다.')
else:
    print('오답입니다.')

# 121
alpabet=input('문자를 입력하시오 :')
if 'a'<=alpabet<='z':
    print(alpabet.upper())
elif 'A'<=alpabet<='Z':
    print(alpabet.lower())

# 122
score=int(input("점수를 입력하시오 :"))
if 81<=score<=100:
    degree='A'
elif 61<=score<=80:
    degree='B'
elif 41<=score<=60:
    degree='C'
elif 21<=score<=40:
    degree='D'
elif 0<=score<=20:
    degree='E'
print(f'grade is {degree}')

# 123
exchange={'달러':1167,'엔':1.096,'유로':1268,'위안':171}
inp=input('입력: ').split()
print(f'{float(inp[0])*exchange[inp[1]]} 원')

# 124
num1=int(input('number1: '))
num2=int(input('number2: '))
num3=int(input('number3: '))
print(max(num1,num2,num3))

# 125
telecom={'011':'SKT','016':'KT','019':'LGU','010':'알수없음'}
phone=input('휴대전화 번호 입력: ').split('-')
print(f'당신은 {telecom[phone[0]]} 사용자입니다.')

# 126
post_number={'0':"강북구",'1':"강북구",'2':"강북구",'3':"도봉구",'4':"도봉구",'5':"도봉구",'6':"노원구",'7':"노원구",'8':"노원구",'9':"노원구"}
inp=input('우편번호: ')
print(post_number[inp[2]])

# 127
iden_number=input('주민등록번호: ')
if iden_number[7]=='1' or iden_number[7]=='3':
    print('남자')
elif iden_number[7]=='2' or iden_number[7]=='4':
    print('여자')

# 128
iden_number=input('주민등록번호: ')
if "00"<=iden_number[8:10]<="08":
    print('서울입니다.')
else:
    print('서울이 아닙니다.')

#129 
iden_number=input('주민등록번호: ')
times=int(iden_number[0])*2+int(iden_number[1])*3+int(iden_number[2])*4+int(iden_number[3])*5+int(iden_number[4])*6+int(iden_number[5])*7+int(iden_number[7])*8+int(iden_number[8])*9+int(iden_number[9])*2+int(iden_number[10])*3+int(iden_number[11])*4+int(iden_number[12])*5
mod=times%11
if int(iden_number[13])==11-mod:
    print('유효하는 주민등록번호입니다.')
else:
    print('유효하지 않는 주민등록번호입니다.')

# 131
# 사과
# 귤
# 수박

# 132
#####
#####
#####

# 133
print('A')
print("B")
print("c")

# 134
print("출력: A" )
print("출력: B" )
print("출력: C" )

# 135
print("변환: a")
print("변환: b")
print("변환: c")

# 136
for i in range(10,31,10):
    print(i)

# 137
for i in range(10,31,10):
    print(i)    

# 138
for i in range(10,31,10):
    print(i)
    print('-------')

# 139
print("++++")
for i in range(10,31,10):
    print(i)

# 140
for i in range(4):
    print("-------")

# 141
tax=[100,200,300]
for i in tax:
    print(i+10)

# 142
menu=["김밥","라면","튀김"]
for i in menu:
    print(f'오늘의 메뉴: {i}')










