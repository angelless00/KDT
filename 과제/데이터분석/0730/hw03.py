import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def pie_plot(region,male,female,fig,i):
    fig[i//2,i%2].pie([male/(male+female),female/(male+female)],autopct='%.1f%%',labels=['남성','여성'],startangle=90)
    fig[i//2,i%2].set(title=region)
    


f=open('gender.csv',encoding='euc_kr')
data=csv.reader(f)


num=0
fig=plt.figure(figsize=(10,25))
per=fig.subplots(5,2)
fig.suptitle('대구광역시 구별 남녀 인구 비율',fontsize=20)

for row in data:
    if '대구광역시' in row[0]:
        region=row[0].split('(')
        male_sum=0
        female_sum=0
        for i in range(106,207):
            male=int(row[i].replace(',',''))
            female=int(row[i+103].replace(',',''))
            male_sum+=male
            female_sum+=female
        print(f'{region[0]} : (남:{male_sum:,} 여:{female_sum:,})')
        pie_plot(region[0],male_sum,female_sum,per,num)
        num+=1

plt.show()
f.close()


