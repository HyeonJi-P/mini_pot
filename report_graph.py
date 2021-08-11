import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

######설치안된것들은 'pip install 설치할것' 으로 커멘드

#def mk_graph(file_name, x_col, y_col, title):
    #파일 읽기
    #데이터 정제?
    #표 사이즈설정 및 그리기
    #타이틀 표시
    #범례?
    #show

#파일 읽기
temp_all = pd.read_csv("./temperature.csv", encoding='cp949')

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
ax = sns.lineplot(x='day',y='lowest', data=temp_del ) #최저기온
ax = sns.lineplot(x='day',y='highest', data=temp_del ) #최고기온
plt.title('July Temperature') #타이틀 표시. 있어도 되고 없어도 되고
plt.legend(labels =['mean', 'lowest', 'highest']) #범례 자동으로 추가가 안되서 명시적으로 설정!
plt.show()
