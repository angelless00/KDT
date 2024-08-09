from bs4 import BeautifulSoup

html_example="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>"""

soup=BeautifulSoup(html_example,'html.parser')

print(soup.title) # title 태그 전체
    #=> <title>BeautifulSoup 활용</title>
print(soup.title.string)    # title 텍스트만
print(soup.title.get_text())    # .string과 동일
    #=><title>BeautifulSoup 활용</title>
print(soup.title.parent)    # 해당태그를 포함하는 부모 출력
# =><head>
#   <meta charset="utf-8"/>
#   <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
#   <title>BeautifulSoup 활용</title>
#   </head>

print(soup.body)    # body만 출력

# <h1> 태그 접근---------------------------------------------------------------------------
print(soup.h1)
print(soup.h1.string)

# <a> 태그 접근-------------------------------------------------------------------------
print(soup.a)   # <a>태그 전체 추출
#=><a class="external_link" href="www.google.com">google</a>
print(soup.a.string) # 태그 내부의 텍스트 추출
#=> google
print(soup.a['href']) # url 추출
print(soup.a.get('href'))   # url 추출 