from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

query='chatGPT'
#query=quote('한글')     # 한글 쓰고싶으면
url=f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={query}'
#reponse=requests.get(url)
#soup=BeautifulSoup(response.text,'html.parser)



html=urlopen(url)
soup=BeautifulSoup(html.read(),'html.parser')
blog_results=soup.select('a.title_link')
print('검색결과수: ',len(blog_results))


# # 제목들고오기 
# for blog_title in blog_results:
#     title=blog_title.text
#     link=blog_title['href']
#     print(f'{title},[{link}]')


# # 내용들고오기

# desc_results=soup.select('a.dsc_link')
# for desc in desc_results:
#     title=blog_results
#     print(desc.text)

search_count=len(blog_results)
desc_results=soup.select('a.dsc_link')

for i in range(search_count):
    title=blog_results[i].text
    link=blog_results[i]['href']
    print(f'{title},[{link}]')
    print(desc_results[i].text)
    print('-'*80)
