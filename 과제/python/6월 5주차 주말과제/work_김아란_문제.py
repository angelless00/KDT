#001 print 기초
print('Hello World')

#002 print 기초
print('Mary\'s cosmetics')

#003 print 기초
print('신씨가 소리질렀다. "도둑이야".')

#004 print 기초
print("c:\\windows")

#005 print 탭과 줄바꿈
print("안녕하세요.\n만나서\t\t반갑습니다.")
# \n => 줄바꿈      \t=>탭

#006 print 여러 데이터 출력
print ("오늘은", "일요일")
#오늘은 일요일

#007 print 기초
print("naver","kakao","sk","samsung",sep=";")

#008 print 기초
print("naver","kakao","sk","samsung",sep="/")

#009 print 줄바꿈
print("first",end='')
print("second")

#010 연산 결과 출력
print(5/3)

#011 변수 사용하기
삼성전자=50000
주식=10
print(삼성전자*주식)

#012 변수 사용하기
시가총액=298000000000000
현재가=50000
PER=15.79
print(시가총액,type(시가총액))
print(현재가,type(현재가))
print(PER,type(PER))

#013 문자열 출력
s = "hello"
t = "python"
print(f'{s}! {t}')

#014 파이썬을 이용한 값 계산
8

#015 type 함수
a="132"
print(type(a))

#016 문자열을 정수료 변환
num_str="720"
result=int(num_str)

#017 정수를 문자열 100으로 변환
num=100
result=str(num)

#018 문자열을 실수로 변환
data="15.79"
result=float(data)

#019 문자열을 정수로 변환
year="2020"
result=int(2020)

#020 파이썬 계산
price=48584
month=36
print(price*month)

#021 문자열 인덱싱
letters = 'python'
print(letters[0],letters[2])

#022 문자열 슬라이싱
license_plate = "24가 2210"
print(license_plate[-4:])

#023 문자열 인덱싱
string = "홀짝홀짝홀짝"
print(string[::2])

#024 문자열 슬라이싱
string = "PYTHON"
print(string[::-1])

#027 문자열 다루기
url = "http://sharebook.kr"
url=url.split('.')
print(url[-1])

#028 문자열은 immutable
lang = 'python'
lang[0] = 'P'
print(lang)
#error

#031 문자열 합치기
a = "3"
b = "4"
print(a + b)
#34

#032 문자열 곱하기
print("Hi" * 3)
#HIHIHI

#033 문자열 곱하기
print('-'*80)

#034 문자열 곱하기
t1 = 'python'
t2 = 'java'
t3=t1+' '+t2+' '
print(t3*4)

#035 문자열 출력
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print('이름: %s 나이: %d'%(name1,age1))
print('이름: %s 나이: %d'%(name2,age2))

#037 문자열 출력
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f'이름: {name1} 나이: {age1} ')
print(f'이름: {name2} 나이: {age2} ')

#039 문자열 슬라이싱
분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])

#047 split 메서드
a = "hello world"
a.split()

#048 split 메서드
ticker = "btc_krw"
ticker.split('_')

#049 split 메서드
date = "2020-05-01"
date.split('-')

#051 리스트 생성
movie_rank=["닥터 스트레인지","스플릿","럭키"]

#054 
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]

#055
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2:]
print(movie_rank)

#056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs=lang1+lang2
print(langs)

#057
nums = [1, 2, 3, 4, 5, 6, 7]
print(F'max: {max(nums)}')
print(F'min: {min(nums)}')

#058
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

#060
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))

#061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#063
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

#064
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])

#069 문자열 split 메서드
string = "삼성전자/LG전자/Naver"
interest=string.split('/')
print(interest)

#070 리스트 정렬
data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))

#071
my_variable=()
print(type(my_variable))

#072
movie_rank=('닥터 스트레인지','스플릿','럭키')

#073
tup=(1,)

#074
>> t = (1, 2, 3)
>> t[0] = 'a'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[0] = 'a'
TypeError: 'tuple' object does not support item assignment
#튜플은 요소 변경이 안됨

#075
t = 1, 2, 3, 4
#튜플

#076
t = ('a', 'b', 'c')
t=list(t)
t[0]='A'
t=tuple(t)
print(t,type(t))

#077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
result=list(interest)

#078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
result=tuple(interest)

#079
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
#apple banana cake

#080
print(tuple(range(2,99,2)))