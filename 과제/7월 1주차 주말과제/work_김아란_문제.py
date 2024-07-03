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

# 143
stock= ["SK하이닉스", "삼성전자", "LG전자"]
for i in stock:
    print(len(i))

# 144
animal= ['dog', 'cat', 'parrot']
for i in animal:
    print(len(i))

# 145
animal= ['dog', 'cat', 'parrot']
for i in animal:
    print(animal[i][0])

# 145
animal= ['dog', 'cat', 'parrot']
for i in animal:
    print(i[0])

# 146
nums = [1, 2, 3]
for i in nums:
    print(f'3x{i}')

# 147
nums = [1, 2, 3]
for i in nums:
    print(f'3x{i}={3*i}')

# 148
word = ["가", "나", "다", "라"]
for i in range(1,len(word)):
    print(word[i])

# 149
word = ["가", "나", "다", "라"]
for i in range(0,len(word),2):
    print(word[i])

# 149
word = ["가", "나", "다", "라"]
for i in range(0,len(word),-1):
    print(word[i])

# 150
word = ["가", "나", "다", "라"]
for i in range(len(word)-1,-1,-1):
    print(word[i])

# 151
nums=[3,-20,-3,44]
for i in nums:
    if i<0:
        print(i)

# 152
nums=[3,100,23,44]
for i in nums:
    if i%3==0:
        print(i)

# 153
nums=[13,21,12,14,30,18]
for i in nums:
    if i<20 and i%3==0:
        print(i)

# 154
msg= ["I", "study", "python", "language", "!"]
for i in msg:
    if len(i)>=3:
        print(i)

# 155
msg = ["A", "b", "c", "D"]
for i in msg:
    if 'A'<=i<='Z':
        print(i)

# 156
msg = ["A", "b", "c", "D"]
for i in msg:
    if 'a'<=i<='a':
        print(i)

# 157
animal = ['dog', 'cat', 'parrot']
for i in animal:
    print(i.upper())

# 158
msg = ['hello.py', 'ex01.py', 'intro.hwp']
for i in msg:
    j=i.split('.')
    print(j[0])

# 159
msg = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in msg:
    j=i.split('.')
    if j[1]=='h':
        print(i)

# 160
file_name = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in file_name:
    j=i.split('.')
    if j[1]=='h' or j[1]=='c':
        print(i)

# 161
for num in range(100):
    print(num)

# 162
for i in range(2002,2051,4):
    print(i)

# 163
for i in range(3,31,3):
    print(i)
    
# 164
for i in range(99,-1,-1):
    print(i)

# 165
for i in range(10):
    print('0.',i,sep='')

# 166
for i in range(1,10):
    print(f'3x{i}={3*i}')

# 167
for i in range(1,10,2):
    print(f'3x{i}={3*i}')

# 168
total=0
for i in range(1,11):
    total=total+i
print(f'합 : {total}')

# 169
total=0
for i in range(1,11,2):
    total=total+i
print(f'합 : {total}')

# 170
total=1
for i in range(1,11):
    total=total*i
print(f'합 : {total}')

# 171
price_list = [32100, 32150, 32000, 32500]
for i in price_list:
    print(i)

# 172
price_list = [32100, 32150, 32000, 32500]
for i,price in enumerate(price_list):
    print(i,price)

# 173
price_list = [32100, 32150, 32000, 32500]
for i,price in enumerate(price_list):
    print(3-i,price)

# 174
price_list = [32100, 32150, 32000, 32500]
for i in range(1,len(price_list)):
    print(90+10*i,price_list[i])

# 175
my_list = ["가", "나", "다", "라"]
for i in range(3):
    print(my_list[i],my_list[i+1])

# 176
my_list = ["가", "나", "다", "라","마"]
for i in range(3):
    print(my_list[i],my_list[i+1],my_list[i+2])

# 177
my_list = ["가", "나", "다", "라"]
for i in range(3):
    print(my_list[3-i],my_list[2-i])

# 178
my_list = [100, 200, 400, 800]
for i in range(3):
    print(my_list[i])

# 179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(4):
    print((my_list[i]+my_list[i+1]+my_list[i+2])/3)

# 180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatilty=[]
for i in range(5):
    volatilty.append(high_prices[i]-low_prices[i])
print(volatilty)

# 181
apart=[['101호','102호'],['201호','202호'],['301호','302호']]

# 182
stock=[["시가",100,200,300],["종가",80,210,330]]

# 183
stock={"시가":[100,200,300],"종가":[80,210,330]}

# 184
stock={"10/10":[80,110,70,90],"10/11":[210,230,190,200]} 

# 185
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in range(3):
    for j in range(2):
        print(apart[i][j],'호')

# 187
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in range(2):
        print(i[j],'호')

# 188
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in i[::-1]:
        print(i[j],'호')

# 188
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j,'호')
        print('-----')

# 189
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j,'호')
    print('-----')

# 190
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j,'호')
print('-----')

# 191 
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data:
    for j in i:
        print(j*1.00014)

# 192 
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data:
    for j in i:
        print(j*1.00014)
    print('----')

# 193 
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result=[]
for i in data:
    for j in i:
        result.append(j*1.00014)
print(result)

# 194 
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result=[]
for i in data:
    sub=[]
    for j in i:
        sub.append(j*1.00014)
    result.append(sub)
print(result)

#195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in range(1,4):
    print(ohlc[i][3])

#196
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in range(1,4):
    if ohlc[i][3]>150:
        print(ohlc[i][3])


#197
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in range(1,4):
    if ohlc[i][3]>=ohlc[i][0]:
        print(ohlc[i][3])


#198
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility=[]
for i in range(1,4):
    volatility.append(ohlc[i][1]-ohlc[i][2])
print(volatility)

#199
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in range(1,4):
    if ohlc[i][3]>ohlc[i][0]:
        print(ohlc[i][3]-ohlc[i][0])

#200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
diff=0
for i in range(1,4):
    diff=diff+ohlc[i][3]-ohlc[i][0]
print(diff)

















