#-----------------------------------------------------------
# 문자열 sr 데이터 다루기
# - 이스케이프문자 : 특수한 의미를 가지는 문자
#   * 형식 : \문자1개
#   *'\n' - 줄바꿈 문자
#   *'\t' - 탭간격 문자
#   *'\'' - 홑따움표 문자
#   *'\"' - 쌍따옴표 문자
#   *'\\' - 백슬러시 문자, 경로(path), URL 관련
#   *'\U' - 유니코드 문자
#   *'\a' - 알람소리 문자
#-------------------------------------------------------
msg="오늘은 좋은날\n내일은\n주말이라\n행복해"
print(f"msg 줄바꿈 : {msg}")

#msg='오늘은 나의 '생일'이야'    <- ''안에 '' 오류!
#print(msg)

msg='오늘은 나의 \'생일\'이야'
print(msg)

#file='C:\Users\KDP-30\Desktop\과제\6.26\test.txt'  <= \한개는 오류
#print(file)

file='C:\\Users\\KDP-30\\Desktop\\과제\\6.26\\test.txt'
print(file)

# r'  ' 또는 R'  ' : 문자열 내 이스케이프 문자는 무시됨!
file=r'C:\Users\KDP-30\Desktop\과제\6.26\test.txt'

msg1="Happy\tNew\tyear"
msg2=r"Happy\tNew\tyear"

print(f'msg1 = {msg1}')
print(f'msg2 = {msg2}')