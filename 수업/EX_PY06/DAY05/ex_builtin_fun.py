#-----------------------------------------------------------------------------------------------
# 내장함수
#-----------------------------------------------------------------------------------------------
## 정수 관련 내장함수-------------------------------------------------------
## 2진수(컴퓨터), 8진수, 10진수(사람), 16진수(프로그램)
# 정수 ==> 2진수 변화해주는 내장함수 bin(정수) ==> 0b숫자 str타입

print(bin(30),type(bin(30)))
#       =>0b11110 <class 'str'>

# 정수 ==> 8진수 변화해주는 내장함수 oct(정수) ==> 0o숫자 str타입
print(oct(30),type(oct(30)))
#       =>0o36 <class 'str'>

# 정수 ==> 16진수 변화해주는 내장함수 hex(정수) ==> 0h숫자 str타입
print(hex(30),type(hex(30)))
#       =>0x1e <class 'str'>

