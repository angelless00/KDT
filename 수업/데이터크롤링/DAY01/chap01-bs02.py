from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html=urlopen('http://www.pythonscraping.com/pages/error.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server coud not be found!')
else:
    print('It worked!')
