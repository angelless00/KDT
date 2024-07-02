#------------------------------------------------------------------------------------------------
# Dict 자료형 살펴보기
# - 데이터의 의미를 함께 저장하는 자료형
# - 형태 : {키1:값, 키2:값, ...., 카n:값}
# - 키는 중복x, 값은 중복 o
# - 데이터 분석 시 파일 데이터 가져 올 때 많이 사용
#------------------------------------------------------------------------------------------------  
## [Dict 생성]----------------------------------------------------------------
data={}
print(f'data=>{len(data)}개, {type(data)},{data}')

# 사람에 대한 정보 : 이름, 나이, 성별
data={'name' : "마징가","age":100,'gender':"남"}
print(f'data=>{len(data)}개, {type(data)},{data}')

# 강아지에 대한 정보 : 품종, 무게, 색상, 성별, 나이
dog={"kind":'시고르잡종',"weight":6.7,"color":"White mix",'gender':"남","age":10}
print(f'data=>{len(dog)}개, {type(dog)},{dog}')

## [Dict 원소/요소 읽기]----------------------------------------------------------------
## - 키를 가지고 값/데이터 읽기
## - 형식 : 변수명 [키]
dog={"kind":'시고르잡종',"weight":6.7,"color":"White mix",'gender':"남","age":10}

# 색상 출력
print(f'색상 : {dog["color"]}')

# 성별, 품종 출력
print(f'성별 : {dog["gender"]}, 품종 : {dog["kind"]}')

## [Dict 원소/요소 변경]-----------------------------------------------------
## -형식 : 변수명[키] = 변경값
#나이 5살 ==> 6살
dog["age"]=6
print(dog)

## [Dict 원소/요소 삭제]-----------------------------------------------------
## - del 변수명[키] 또는 del(변수명[키])
del dog["gender"]
print(dog)

## 추가 : 변수명 [새로운 키] = 값-------------------------
## 이름추가
dog["name"]="뽀삐"
print(dog)

