students=[('Alice',3.9,20160303),
          ('Bob',3.0,20160302),
          ('Charlie',4.3,20160301)]

# 학번(students[2])을 기준으로 오름차순 정렬
print('-'*50)
print('sorted key 입력 없음')
print(sorted(students))
print('-'*50)

sorted_studen1=sorted(students,key=lambda s:s[2])
print(sorted_studen1)

# 학점(students[1])을 기준으로 오름차순 정렬
sorted_studen2=sorted(students,key=lambda s:s[1])
print(sorted_studen2)


