# p.49 3.7 연습문제 : 문자열 출력하기

print('Hello, world!')
print('Python Programming')

# p.49 3.8 심사문제 :문자열 출력하기

print('Hello, world!')
print('Hello, world!')

# p.62 5.5 연습문제 : 아파트에서 소음이 가장 심한 층수 출력하기
dist=12
print(int(0.2467*dist+4.159))

# p.62 5.6 심사문제 : 스킬 공격력 출력하기
AP=102
print(AP*0.6+225)

# p.70 6.3.4 입력값을 정수로 변환하기
a=int(input('첫 번째 숫자를 입력하세요:'))
b=int(input('두 번째 숫자를 입력하세요:'))
print(a+b)

# p.70 6.4 입력 값을 변수 두 개에 저장하기
a,b=input('문자열 두 개를 입력하세요:').split()
print(a)
print(b)

# p.71 6.4.1 두 숫자의 합 구하기
a,b=input('숫자 두 개를 입력하세요:').split()
print(a+b)

# p.72 6.4.2 입력 값을 정수로 변환하기
a,b=input('숫자 두 개를 입력하세요:').split()
a=int(a)
b=int(b)
print(a+b)

# p.72 6.4.3 map을 사용하여 정수로 변환하기
a,b=map(int,input('숫자 두 개를 입력하세요:').split())
print(a+b)

# p.73 6.4.4 입력받은 값을 콤마를 기준으로 분리하기
a,b=map(int,input('숫자 두 개를 입력하세요:').split(','))
print(a+b)

# p.75 6.6 연습문제 : 정수 세개를 입력받고 합계 출력하기
a,b,c=map(int,(input('').split()))
print(a+b+c)

# p.75 6.7 심사문제 : 변수만들기
a,b,c=(input('')).split()
print(a)
print(b)
print(c)

# p.75 6.8 심사문제 : 평균 점수 구하기
a,b,c,d=map(int,input().split())
print((a+b+c+d)/4)

# p.79 7.2.1 end 사용하기
print(1,end='')
print(2,end='')
print(3,end='')

# p.80 7.4 연습문제 : 날짜와 시간 출력하기
year=2000
month=10
day=27
hour=11
minute=43
second=59

print(year,month,day,sep='/',end='')
print(hour,minute,second,sep=':')

# p.81 7.5 심사문제 : 날짜와 시간 출력하기
year,month,day,hour,minute,second=input().split()
print(year,month,day,sep='-',end='T')
print(hour,minute,second,sep=':')

# p.94 8.4 연습문제 : 합격 여부 출력하기
korean=92
english=47
mathematics=86
science=81
print(korean>=50 and english>=50 and mathematics>=50 and science>=50)

# p.95 8.5 심사문제 : 합격 여부 출력하기
korean,english,mathematics,science=map(int,input().split())
print(korean>=90 and english>80 and mathematics>85 and science>=80)

# p.100 9.3 연습문제 : 여러 줄로 된 문자열 사용하기
s='''python is a programming language that lets you work quickly
and
integrate systems more effectively.'''
print(s)

# p.101 9.4 심사문제 : 여러 줄로 된 문자열 사용하기
s=''''Python' is a "programing language"
that lets you work quickly
and
integrate systems mork effectively.'''
print(s)