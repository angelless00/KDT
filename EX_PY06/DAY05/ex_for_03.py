#-----------------------------------------------------------------------------------------------
# 제어문 - 반복문
#-----------------------------------------------------------------------------------------------
# [실습] 출력하고 싶은 단을 입력 받아서 해당 단의 구구단을 출력하세요.
# [출력예시] 2*1=2

gugudan=int(input("몇 단? : "))
for i in range(1,10):
    print(f'{gugudan}*{i}={gugudan*i}')