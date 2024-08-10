from bs4 import BeautifulSoup
from urllib.request import Request
from urllib.request import urlopen


html=urlopen(Request('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yst5ji9yxTY'))
soup=BeautifulSoup(html,'html.parser')

def scraping_use_find(html):
    allfind=soup.find_all("div",{'class':'tombstone-container'})
    for prt in allfind:
        period=prt.find('p',{'class':'period-name'})
        short=prt.find('p',{'class':'short-desc'})
        if prt.find('p',{'class':'temp temp-low'})==None:
            temp=prt.find('p',{'class':'temp temp-high'})
        else:
            temp=prt.find('p',{'class':'temp temp-low'})
        
        img=prt.find('img')
        print('-'*50)
        print('[Period]',period.string,sep=': ')
        print('[Short desc]',short.string,sep=': ')
        print('[Temperature]',temp.string,sep=': ')
        print('[Image desc]: ',img.attrs['title'])




def scraping_use_select(html):
    allselect=soup.select('div.tombstone-container')
    for i in allselect:
        period=i.select_one('p.period-name')
        short=i.select_one('p.short-desc')
        temp=i.select_one('p.temp')
        img=i.select_one('img')
        print('-'*50)
        print('[Period]',period.string,sep=': ')
        print('[Short desc]',short.string,sep=': ')
        print('[Temperature]',temp.string,sep=': ')
        print('[Image desc]: ',img.attrs['title'])
      
        



scraping_use_find(html)

scraping_use_select(html)


