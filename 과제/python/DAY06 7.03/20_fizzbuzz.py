# p.221 20.3 3과 5의 공배수 처리하기 
for i in range(1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

# p.223 코드 단축하기
for i in range(1,101):
    print('Fizz'*(i%3==0)+'Buzz'*(i%5==0)or i)