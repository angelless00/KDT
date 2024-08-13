import requests
from bs4 import BeautifulSoup

import collections

if not hasattr(collections,'callable'):
    collections.Callable=collections.abc.Callable

# 시가 총액 메뉴에서 상위 10개기업 크롤링
url='https://finance.naver.com/sise/sise_market_sum.naver'
html=requests.get(url)
soup= BeautifulSoup(html.text,'html.parser')

company_name=soup.find('tbody').find_all('a',{'class':'tltle'})


company_name=company_name[:10]
high_company=[]
for Cname in company_name:
    high_company.append([Cname.string,Cname.attrs['href']])


def search_com(num):
    search_url=high_company[num-1][1]
    search_html=requests.get('https://finance.naver.com'+search_url)
    search_soup= BeautifulSoup(search_html.text,'html.parser')
    #종목코드
    code=search_soup.find('div',{'class':'description'}).find('span').string
    #현재가
    now=search_soup.find('div',{'class':'rate_info'}).find('p',{'class','no_today'}).find('span',{'class':'blind'}).string
    #전일가
    yesterday=search_soup.find_all('td',{'class':'first'})[0].find('span',{'class':'blind'}).string
    #시가
    market_price=search_soup.find_all('td',{'class':'first'})[1].find('span',{'class':'blind'}).string
    #고가
    high=search_soup.find('div',{'class':'rate_info'}).find_all('tr')[0].find_all('span',{'class','blind'})[1].string
    #저가
    low=search_soup.find('div',{'class':'rate_info'}).find_all('tr')[1].find_all('span',{'class','blind'})[1].string
    print('https://finance.naver.com'+high_company[num-1][1])
    print(f'종목명: {high_company[num-1][0]}')
    print(f'종목코드: {code}')
    print(f'현재가: {now}')
    print(f'전일가: {yesterday}')
    print(f'시가: {market_price}')
    print(f'고가: {high}')
    print(f'저가: {low}')


def prt_com():
    cnt=1
    print('-'*40)
    print('[ 네이버 코스피 상위 10대 기업 목록 ]')
    print('-'*40)
    for com in high_company:
        print(f'[{cnt:2}] {com[0]}')
        cnt+=1

def search():
    while True:
        prt_com()
        num=int(input('주가를 검색할 기업의 번호를 입력하세요(-1: 종료) :'))
        if num==-1:
            break
        else:
            search_com(num)

search()
