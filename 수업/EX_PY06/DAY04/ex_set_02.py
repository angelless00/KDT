#------------------------------------------------------------------------------------------------
# Set 자료형 살펴보기
# - 연산자
#------------------------------------------------------------------------------------------------   
d1={1,3,5,7}
d2={1,2,3,4,6,7}

## 덧셈연산 ==> 합집합
#print(d1+d2) => 지원x => 메서드 사용
print(d1.union(d2),d1|d2)

## 공통원소 ==> 교집합
print(d1.intersection(d2),d1&d2)

## 차집합
print(d1.difference(d2),d1-d2)


## add() 메서드
print(d1.add(d2))






