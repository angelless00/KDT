#----------------------------------
# 입력 & 출력 실습
#-----------------------------------------
# [실습1] 데이터 저장 및 변수 생성
# - 생년월일
# - 띠 
# - 혈액형
# - 출력형태
#   나는 0000년 00월 00일 00띠입니다.1
#   혈액형은 ____형입니다.
#------------------------------------------
birth=input('생년월일을 입력하시오')
Z_sign=input('본인의 띠를 입력하시오')
bloodtype=input('혈액형을 입력하시오.')

print(f"나는 {birth} {Z_sign}입니다.")
print(f"혈액형은 매력적인 {bloodtype}입니다.")

#[실습2] 입력 받은 데이터 저장 단, 파일로 저장
# - 좋아하는 계절
# - 좋아하는 나라
# - 여행가고싶은 나라
# --------------------------------

season=input('좋아하는 계절을 입력하시오.')
f_nation=input('좋아하는 나라를 입력하시오.')
w_nation=input('여행가고 싶은 나라를 입력하시오.')

FILENAME='travel.txt'
f=open(FILENAME,mode='w',encoding='utf-8')
print(f"{season}을 사랑하고 {f_nation}을 좋아하며 {w_nation}을 가고싶어합니다.",file=f)
f.write(season)
f.write('\n')
f.write(f_nation)
f.write('\n')
f.write(w_nation)
f.close()