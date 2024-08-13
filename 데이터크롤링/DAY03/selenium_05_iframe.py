from selenium import webdriver
from bs4 import BeautifulSoup

# callable 에러
import collections

if not hasattr(collections,'callable'):
    collections.Callable=collections.abc.Callable

driver=webdriver.Chrome()
driver.get('https://blog.naver.com/swf1004/221631056531')

driver.switch_to.frame('mainFrame')

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')

results=soup.find_all('div',{'class':'se-module'})

result1=[]
for result in results:
    remove_carriage_str=result.text.replace('\n','')
    print(remove_carriage_str)
    result1.append(remove_carriage_str)

