import pandas as pd
from tabulate import tabulate

cafe_data=pd.read_csv('hollys_branches.csv')


while True:
    inp=input('검색할 매장의 지역을 입력하세요: ').split(' ')
    if inp[0]=='quit':
        break
    else:
        search_data=pd.DataFrame(columns=['매장이름','지역','주소','전화번호'])
        count=1
        for row in cafe_data.index:
            TF=1
            for i in range(len(inp)):
                TF=TF*(inp[i] in cafe_data.loc[row,'주소'])
            if TF==1:
                search_data.loc[count]=cafe_data.iloc[row]
                count+=1
        print(tabulate(search_data,headers='keys',tablefmt='psql')) 
                
    









