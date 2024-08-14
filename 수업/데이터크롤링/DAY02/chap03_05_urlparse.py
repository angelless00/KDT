from urllib.parse import urlparse
"""
scheme: 'http' 또는 'https

netloc: 인터넷 주소

"""



urlString1='https://shopping.naver.com/home/p/index.naver'

url=urlparse(urlString1)
print(url.scheme)   # https
print(url.netloc)   # shopping.naver.com
print(url.path)     # /home/p/index.naver