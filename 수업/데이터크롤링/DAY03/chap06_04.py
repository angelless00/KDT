# 테이블 데이터  CSV로 저장

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs=BeautifulSoup(html,'html.parser')

table=bs.find('table',{'class':'wikitable'})
rows=table.find_all('tr')

csvFile=open('editors.csv','wt',encoding='utf-8')   # t: text mode
writer=csv.writer(csvFile)

try:
    for row in rows:
        csvRow=[]
        for cell in row.find_all(['th','td']):
            print(cell.text.strip())
            csvRow.append(cell.text.strip())        
        writer.writerow(csvRow)
finally:
    csvFile.close()

