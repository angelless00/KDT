#-----------------------------------------------------------------------------------------------
# dictionary 전용 함수 즉, 메서드
# -> keys(), values(), items()
#-----------------------------------------------------------------------------------------------

person={'name':'홍길동', 'age':10}

# [메서드 - 값 읽어오는 메서드 get(key,defalut)]--------------------------------------------
# - key에 해당하는 value가 없으면 defalut 값을 반환
print(person['name'])
# print(person['gender'])  #KeyError

print(person.get('name','몰라'))
print(person.get('gender','없음'))
print(person.get('gender'))


msg="Hello Good Luck"
alpha=set(msg)
save={}
print(alpha)
for m in alpha:
    print(m,msg.count(m))
    save[m]=msg.count(m)
print(save)
 






