#------------------------------------------------------------
#내장함수 print() 사용법
#-print함수의 매개변수 알아보기
#-file 매개변수 :데이터를 파일에 기록
#--------------------------------------------------------
# 파일 읽기 & 쓰기
#-파일열기 open()
#-파일 읽기 또는 쓰기
#-파일 닫기 close()

FILENAME='result.txt'  #중요한 변수일땐 대문자(지우지마!!)
f=open(FILENAME,mode='w') #open()은 기본적으로 읽기파일로 열림! 쓰기모드로 바꿔줘
f.write("HELLO~")
print("Good Luck",file=f) #파일에 데이터 출력하기
f.close() #파일 닫기