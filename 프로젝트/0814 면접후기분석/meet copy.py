from bs4 import BeautifulSoup
import requests
import pandas as pd

import collections

if not hasattr(collections,'callable'):
    collections.Callable=collections.abc.Callable


def tistory(url,job_data):
    html=requests.get(url)
    soup=BeautifulSoup(html.text,'html.parser')
    try:
        #제목뽑기
        if soup.find('h3') is not None:
            title=soup.find('h3').text
        elif soup.find('h2') is not None:
            title=soup.find('h2').text
        elif soup.find('h1') is not None:
            title=soup.find('h1').text
        # 내용 뽑기
        if soup.find('article') is not None:
            article=soup.find('article').text.replace('\n','').replace('\t','')
        else:
            article=soup.find('body').text.replace('\n','').replace('\t','')
        job_data.append([url,title,article])
        print(1)
    except:
        print('예외발생')
    


def naver(end_page,job):
    page=2
    job_data=[]
    while page<=end_page:
        url=f'https://search.naver.com/search.naver?nso=&page={page}&query=tistory.com+{job}+면접후기&sm=tab_pge&start={15*(page-2)+1}&where=web'
        html=requests.get(url)
        soup=BeautifulSoup(html.text,'html.parser')
        # 링크 리스트를 뽑아냄
        link_list=soup.find_all('a',{'class':'link_tit'})
        for i in range(len(link_list)):
            link=link_list[i].attrs['href']
            tistory(link,job_data)
        page+=1
    job_dataDF=pd.DataFrame(job_data,columns=['주소','제목','내용'])
    return job_dataDF

# 개발자 면접후기 추출
# developer=naver(10,'개발자')
# developer.to_csv('developer.csv')

# 데이터 사이언티스트 면접후기 추출
# datamining=naver(10,'데이터사이언티스트')
# datamining.to_csv('datascientist.csv')

# 데이터 엔지니어 면접후기 추출
datamining=naver(10,'데이터엔지니어')
datamining.to_csv('dataengineer.csv')


    