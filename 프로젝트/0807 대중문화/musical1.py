import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

conn=pymysql.connect(host='localhost',user='member2',password='1234',db='sql_project',charset='utf8')
curs=conn.cursor(pymysql.cursors.DictCursor)

# 테이블을 가져와 데이터 프레임으로 만드는 함수
def DF(table,idx):
    sql=f"select * from {table}"
    curs.execute(sql)
    rows=curs.fetchall()     # 모든 데이터를 불러옴
    table_DF=pd.DataFrame(rows)
    table_DF.set_index(idx,inplace=True)
    return table_DF

musical_oversea_DF=DF('musical_oversea','지역')
musical_small_DF=DF('musical_small','지역')
musical_large_DF=DF('musical_large','지역')


# 티켓판매금액 평균을 구하는 함수
def avg(df):
    avg=round(df['총 티켓판매액']/df['총 티켓판매수']*1000,2)
    return avg

oversea_avg_price=avg(musical_oversea_DF)
small_avg_price=avg(musical_small_DF)
large_avg_prince=avg(musical_large_DF)

avg=pd.concat([oversea_avg_price,large_avg_prince,small_avg_price],axis=1)

# nan 값을 0으로 조정
avg.replace(np.nan,0,inplace=True)

# sql에 avg 테이블 입력
# for row in avg.index:
#     sql=f"""insert into musical_avg_price(region,oversea_avg_price,large_avg_price,small_avg_price) 
#         values('{row}',{avg.loc[row,0]},{avg.loc[row,1]},{avg.loc[row,2]})"""
#     curs.execute(sql)
#     conn.commit()

# 평균값그래프
# x=pd.Series(list(range(8)))
# plt.figure(figsize=(10,10))
# plt.bar(x-0.2,avg[0],width=0.2,label='내한뮤지컬')
# plt.bar(x,avg[1],width=0.2,label='대극장뮤지컬')
# plt.bar(x+0.2,avg[2],width=0.2,label='소극장뮤지컬')
# plt.xticks(x,avg.index)
# plt.xlabel('지역',fontsize=15)
# plt.ylabel('평균가격',fontsize=15)
# plt.title('2023 지역별 뮤지컬 평균가격',fontsize=20)
# plt.legend()
# plt.grid()
# plt.show()

def plot3(data):
    x=pd.Series(list(range(7)))
    plt.figure(figsize=(10,10))
    plt.bar(x-0.2,musical_oversea_DF[data][:-1],width=0.2,label='내한뮤지컬')
    plt.bar(x,musical_large_DF[data][:-1],width=0.2,label='대극장뮤지컬')
    plt.bar(x+0.2,musical_small_DF[data][:-1],width=0.2,label='소극장뮤지컬')
    plt.xticks(x,avg.index[:-1])
    plt.xlabel('지역',fontsize=15)
    plt.ylabel(data,fontsize=15)
    plt.title(f'2023 지역별 뮤지컬 {data}',fontsize=20)
    plt.legend()
    plt.grid()
    plt.show()

# plot3('개막편수')
# plot3('상연횟수')
plot3('판매수')

popular_music_DF=DF('popular_avg','region')
wage_DF=DF('region_wage','region')
theater_DF=DF('theater','지역')

# # 최종그래프
# plt.figure(figsize=(10,10))
# x=pd.Series(list(range(7)))
# fig,ax_1=plt.subplots()
# ax_1.set_title('지역별 평균임금과 평균 문화가격비교',fontsize=20)
# ax_1.bar(x-0.2,popular_music_DF['large'],width=0.2,label='대형콘서트')
# ax_1.bar(x,avg[1][:-1],width=0.2,label='대극장뮤지컬')
# ax_1.bar(x+0.2,theater_DF['평균티켓가격'],width=0.2,label='연극')
# ax_1.set_xlabel('지역')
# ax_1.set_ylabel('평균티켓가격')
# ax_1.legend()
# ax_2=ax_1.twinx()
# ax_2.plot(wage_DF['wage'],marker='o',label='평균임금',color='r')
# ax_2.legend(loc=2)
# ax_2.set_ylabel('평균임금')
# ax_2.set_yticks([0,1000000,2000000,3000000,4000000])
# plt.show()




curs.close()
conn.close()