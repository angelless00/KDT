# 예제 : 단어 분석 및 Word Cloud 생성 #1

from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd


file='developer.csv'
#file='datascientist.csv'
#file='dataengineer.csv'
data=pd.read_csv(file)
text=''
for row in data.index:
    text=text+data.loc[row,'내용']

okt=Okt() # Open Korean Text 객체 생성


sentences_tag=okt.pos(text)

noun_adj_list=[]
# tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어준다.
for word,tag in sentences_tag:
    if tag =='Noun':
        noun_adj_list.append(word)

# 가장 많이 나온 단어부터 50개를 저장한다.
counts=Counter(noun_adj_list)
tags=counts.most_common(80)
print(tags)


# 한글을 분석하기위해 font를 한글로 저장
path=r'c:\Windows\Fonts\malgun.ttf'

wc=WordCloud(font_path=path,width=400,height=400,
             background_color='white',max_font_size=200,
             repeat=True,
             colormap='inferno')
dict_tags=dict(tags)
# 제외단어
word_pop=['면접','후기','것','글','수','내','댓글','및','글']
#개발자
#word_pop.append('개발자')

for word in word_pop:
    dict_tags.pop(word)


cloud=wc.generate_from_frequencies(dict_tags)




plt.figure(figsize=(10,8))
plt.axis('off')
plt.imshow(cloud)
plt.show()




