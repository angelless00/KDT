import pymysql
import pandas as pd
import csv

conn=pymysql.connect(host='localhost',user='root',password='1234',db='sakila',charset='utf8')
cur=conn.cursor()
cur.execute('select * from language')

desc=cur.description # 헤더정보 가져옴
for i in range(len(desc)):
    print(desc[i][0],end=' ')
print()

rows=cur.fetchall() # 모든 데이터를 가져옴
for data in rows:
    print(data)
print()

cur.close()
conn.close()  # 데이터 베이스 연결 종료

## 주피터갈래 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ