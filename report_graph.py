import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

######설치안된것들은 'pip install 설치할것' 으로 커멘드

#csv파일 읽기
temp_all = pd.read_csv("./mini_pot/temperature.csv", encoding='cp949')

#필요없는 컬럼 제거(지점)
temp_del=temp_all.drop(columns={'지점'})

#날짜 쪼개기
month =[]
day = []
for data in temp_del['Date']:
    month.append(data.split('-')[1])
    day.append(data.split('-')[2])

temp_del['month']=month
temp_del['day']=day

temp_del['month'].astype('int64') #필요한지 몰라서 일단 썼음
temp_del['day'].astype('int64')

print(temp_del)

# seaborn의 countplot 함수를 사용하여 출력
#한국어 출력은 폰트설정 필요

plt.figure(figsize=(10,5)) #표 사이즈
sns.set(style="darkgrid") #스타일 설정
ax = sns.lineplot(x='day',y='mean', data=temp_del) #평균기온
ax = sns.lineplot(x='day',y='lowest', data=temp_del) #최저기온
ax = sns.lineplot(x='day',y='highest', data=temp_del) #최고기온
plt.show()