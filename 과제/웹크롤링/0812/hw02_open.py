from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

f=open('hollys_branches.csv',mode='w',encoding='utf-8')
count=1
f.write('매장이름,지역,주소,전화번호\n')
for i in range(1,51):
    url=f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
    html=urlopen(url)
    soup=BeautifulSoup(html,'html.parser')

    table=soup.find('tbody')
    info_list=table.find_all('td',{'class':'center_t'})

    for i in range(len(table.find_all('td',{'class':'noline center_t'}))):
        f.write(f'{info_list[6*i+1].string},{info_list[6*i+0].string},{info_list[6*i+3].string},{info_list[6*i+5].string}\n')
        
        print(f'[{count:3}]: 매장이름: {info_list[6*i+1].string}, 지역: {info_list[6*i+0].string}, 주소: {info_list[6*i+3].string}, 전화번호: {info_list[6*i+5].string}')
        count+=1

print(f'전체 매장 수: {count-1}')



f.close()

print(f'hollys_branches.csv 파일 저장 완료')








