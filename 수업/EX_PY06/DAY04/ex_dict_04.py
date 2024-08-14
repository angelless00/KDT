#------------------------------------------------------------------------------------------------
# Dict 자료형 살펴보기 
# - 연산자와 내장함수
# 
#------------------------------------------------------------------------------------------------ 
person={'name':'홍길동','age':20,'job':'학생'}
dog={"kind":'시고르잡종',"weight":6.7,"color":"White mix",'gender':"남","age":10}
jumsu={'국어':90,"수학":178,"체육":100}

## [연산자]--------------------------------------------------------
# 산술 연산 x
# person+dog ====> xx

# 멤버 연산자 : in, not in
#      key
print('name' in dog)
print('name' in person)

##      value  =================> dict 타입에서는 key만 멤버연산자 가능
#print('시고르잡종'in dog)
#print(20 in person)

# value 추출
print('시고르잡종' in dog.values())

## [내장함수]--------------------------------------------------------
## -원소/요소 갯수 확인 : len()
print(f'dog의 요소 갯수 : {len(dog)}')
print(f'person의 요소 갯수 : {len(person)}')

## -원소/요소 정렬 : sorted() 
#       ===> 키로만 정렬 후 키 만 추출
print(f'dog 정렬 :{sorted(dog)}')
print(f'dog 내림차순 정렬 :{sorted(dog)},reversed=True')

#print(f'dog 정렬 :{sorted(dog.values())}')
#               ==> value들의 타입이 달라서 정렬 불가
print(f'jumsu 키 오름차순정렬 :{sorted(jumsu)}')
print(f'jumsu 값 오름차순정렬 :{sorted(jumsu.values())} ')
print(f'jumsu 값 오름차순정렬 :{sorted(jumsu.items())} ')
#       =>jumsu 값 오름차순정렬 :[('국어', 90), ('수학', 178), ('체육', 100)]
# 값을 기준으로 정렬하고 싶을때
print(f'jumsu 값 오름차순정렬 :{sorted(jumsu.items(),key=lambda x:x[1])} ')
#       =>jumsu 값 오름차순정렬 :[('국어', 90), ('체육', 100), ('수학', 178)]

## 동일한 타입에 한해서 정렬 가능
n1=[1,4,9,2]
n2=['a','z','f']
n3=[1,'A',-4,9,'F']
# n3는 sorted 불가!






