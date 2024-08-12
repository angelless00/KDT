from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd

count=0
cafe=pd.DataFrame(columns=['매장이름','지역','주소','전화번호'])

for i in range(1,51):
    url=f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
    html=urlopen(url)
    soup=BeautifulSoup(html,'html.parser')

    table=soup.find('tbody')
    info_list=table.find_all('td',{'class':'center_t'})

    for i in range(len(table.find_all('td',{'class':'noline center_t'}))):
        adress=info_list[6*i+3].string.replace('\"','')
        name=info_list[6*i+1].string
        country=info_list[6*i+0].string
        phone=info_list[6*i+5].string
        cafe.loc[count]=[name,country,adress,phone]
        print(f'[{count+1:3}]: 매장이름: {name}, 지역: {country}, 주소: {adress}, 전화번호: {phone}')
        count+=1

print(f'전체 매장 수: {count}')
cafe.to_csv('hollys_branches.csv',index=False)




print(f'hollys_branches.csv 파일 저장 완료')








