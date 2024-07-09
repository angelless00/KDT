import random

correct_answer=set()
while len(correct_answer)<3:
    num=random.randint(0,9)
    correct_answer.add(num)
correct_answer=list(correct_answer)
print(correct_answer)

strike=0
while strike!=3:
    ball=0
    strike=0
    sol0,sol1,sol2=map(int,input('세자리 숫자를 입력하시오 : ').split())
    if sol0==correct_answer[0]:
        strike=strike+1
    if sol1==correct_answer[1]:
        strike=strike+1
    if sol2==correct_answer[2]:
        strike=strike+1
    if sol0==correct_answer[1] or sol0==correct_answer[2]:
        ball=ball+1
    if sol1==correct_answer[0] or sol1==correct_answer[2]:
        ball=ball+1
    if sol2==correct_answer[0] or sol2==correct_answer[1]:
        ball=ball+1
    print(f'{strike}스트라이크 {ball}볼')