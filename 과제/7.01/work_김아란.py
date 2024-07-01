# p.149 12.4 연습문제 : 딕셔너리에 게임 캐릭터 능력치 저장하기
camille={'health':575.6,'heath_regen':1.7,'mana':338.8,'mana_regen':1.63,'melee':125,'attack_damage':60,"attack_speed":0.625,'armor':26,'magic_resistance':32.1,"movement_Speed":340}
print(camille['health'])
print(camille['movement_Speed'])

# p.150 12.5 심사문제 : 딕셔너리에 게임 캐릭 터 능력치 저장하기
menu=input().split()
data=map(float,input().split())
charicter=dict(zip(menu,data))
print(charicter)

# p.160 
x=10

if x==10:
    print('x에 들어있는 숫자는')
    print('10입니다.')

# p.161 중첩 if 조건문 사용하기
x=15
if x>=10:
    print('10이상입니다.')
    if x==15:
        print('15입니다.')
    if x==20:
        print('20입니다.')

# p.163 사용자가 입력한 값에 if 조건문 사용하기
x=int(input())
if x==10:
    print('10입니다.')
if x==20:
    print('20입니다.')

# p.164 연습문제 : if 조건문 사용하기
x=5
if x!=10:
    print('OK')

# p.165 심사문제 : 온라인 할인 쿠폰 시스템 만들기
price=int(input())
coupon=input()
if coupon=='Cash3000':
    print(price-3000)
elif coupon=='Cash5000':
    print(price-5000)

# p.168 else와 들여쓰기
x=10

if x==10:
    print('10입니다.')
else:
    print('x에 들어있는 숫자는')
    print('10이 아닙니다')

# p.169 if 조건문의 동작 방식 알아보기
if True:
    print('참')
else:
    print('거짓')

if False:
    print('참')
else:
    print('거짓')

if None:
    print('참')
else:
    print('거짓')

# p.170 if 조건문에 숫자 지정하기
if 0:
    print('참')
else:
    print('거짓')

if 1:
    print('참')
else:
    print('거짓')

if 0x1F:
    print('참')
else:
    print('거짓')

if 0b1000:
    print('참')
else:
    print('거짓')

if 13.5:
    print('참')
else:
    print('거짓')

# p.170 if 조건문에 문자열 지정하기
if "Hello":
    print('참')
else:
    print('거짓')

if '':
    print('참')
else:
    print('거짓')

# p.172 조건식을 여러 개 지정하기
x=10
y=20

if x==10 and y==20:
    print('참')
else: 
    print('거짓')

# p.174 연습문제 : 합격 여부 판단하기
written_test=75
coding_test=True
if written_test>=80 and coding_test==True:
    print('합격')
else:
    print('불합격')

# p.174 심사문제 : 합격 여부 판단하기
score=list(map(int,input().split()))
aver=sum(score)/len(score)
score_range=range(0,101)
if score[0] in score_range and score[1] in score_range and score[2] in score_range and score[3] in score_range:
    if aver>=80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')

# p.177 if,elif,else 모두 사용하기
x=30

if x==10:
    print('10입니다.')
elif x==20:
    print('20입니다.')
else:
    print('10도 20도 아닙니다.')

# p.178 음료수 자판기 만들기
button=int(input())

if button==1:
    print('콜라')
elif button==2:
    print('사이다')
elif button==3:
    print('환타')
else:
    print('제공하지 않는 메뉴')

# p.180 연습문제 : if, elif, else 모두 사용하기
x=int(input())
if x>=11 and x<=20:
    print('11~20')
elif x>=21 and x<=30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

# p.180 심사문제 : 교통카드 시스템 만드기
age=int(input())
balance=9000
if age>=7 and age<=12:
    print(balance-650)
elif age>=13 and age<=18:
    print(balance-1050)
else:
    print(balance-1250)

