#-----------------------------------------------------------------------------------------------
# 람다표현식 또는 람다함수
# - 1줄 함수, 익명 함수
# - 형식 : lambda 매개변수 : 실행코드
#-----------------------------------------------------------------------------------------------
names={1:'Kim',2:'Adam',3:'Zoo'}

# 정렬하기 => 내장함수 sorted() --->list반환
# [기본] key로 정렬
result=sorted(names)
print(f'오름차순 정렬 [Key] {result}')

# value로 정렬 => names.items() -->(1,'Kim'),(2,'Adam'),(3,'Zoo')
result=sorted(names.items(),key=lambda items:items[1])
print(f'오름차순 정렬 [Value] {result}')

result=sorted("This is a test string from Andrew".split())
print(result)
result=sorted("This is a test string from Andrew".split(),key=str.lower)
print(result)

## map()와 lambda-------------------------------------------------------------------
data=[11,22,33,44]

# - 각 원소의 값에 곱셈 곱하기 2해서 다시 리스트로 저장
# def multi2(value):                    =>한번쓸거 왜 정의함?
#     return value*2

# data2=list(map(multi2,data))
# print(data2)

data2=list(map(lambda a:a*2,data))  #람다 함수로 해결
