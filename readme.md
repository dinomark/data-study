### matplotlib.pyplot 사용하기

import matplotlib.pyplot as plt

plt.plot([10,20,30,40])
plt.show()

plt.plot([1,2,3,4],[14,25,34,26])
plt.title('plotting')
plt.show()

plt.title('plotting')
plt.plot([40,30,20,10], color='red', label='desc')
plt.plot([10,20,30,40], color='blue', label='asc')
plt.legend(loc=5)
plt.show()

plt.title('line style')
plt.plot([40,30,20,10], color='skyblue', label='Desc', ls=':')
plt.plot([10,20,30,40], color='orange', label='Asc', linestyle='--')
plt.legend()
plt.show()

plt.title('marker')
plt.plot([10,20,30,40], 'r^--', label='red triangle dash')
plt.plot([40,30,20,10], 'g.:', label='sb dot dot')
plt.legend()
plt.show()

### 내 생일의 기온들을 하나의 그래프로 그려보자

import pandas as pd
import csv 

f = open('C:/Users/victo/OneDrive - 강원대학교/허룡이의 코딩생활/데이터분석 스터디/불러오기 자료/seoul.csv')
data=csv.reader(f)

# for row in data:
#     print(row)
    
next(data)

result = [] # 최고기온 데이터를 저장할 리스트

for row in data:
    if row[-1] != '':
        result.append(float(row[-1]))
        
len(result)

### 얻은 데이터들을 꺾은선 그래프로 표시해보자

import matplotlib.pyplot as plt

plt.figure(figsize=(20,5))
plt.plot(result, color='r')
plt.title('hotest temp')
plt.ylabel('Celcius')
plt.show()

#### 8월의 최고기온 데이터만을 이용해 그래프를 다시 그려보자 split 함수를 이용한다

f = open('C:/Users/victo/OneDrive - 강원대학교/허룡이의 코딩생활/데이터분석 스터디/불러오기 자료/seoul.csv')

data = csv.reader(f)

next(data)

result=[]

for row in data:
    if((row[0].split('-')[1]) == '08'):
        if row[-1] != '':
            result.append(float(row[-1]))

print(result)
print(len(result))

plt.figure(figsize=(20,5))

plt.plot(result, color='r')
plt.title('August temp')

plt.show()

#### 지금까지 그래프를 다루는 연습을 했으니, 실제로 내 생일을 기준으로 내 생일의 최고기온만을 나타내는 그래프를 그려보자

f = open('C:/Users/victo/OneDrive - 강원대학교/허룡이의 코딩생활/데이터분석 스터디/불러오기 자료/seoul.csv')

data = csv.reader(f)

next(data)

result=[]

for row in data:
    if (row[0].split('-')[1] == '10') & (row[0].split('-')[2] == '02'):
        if(row[-1]) != '':
            result.append(float(row[-1]))
            
print(result)

plt.figure(figsize=(20,5))

plt.plot(result, 'r.--')
plt.title('my birthdat temp')
plt.ylabel('Celcius')
plt.show()

f = open('C:/Users/victo/OneDrive - 강원대학교/허룡이의 코딩생활/데이터분석 스터디/불러오기 자료/seoul.csv')

data = csv.reader(f)

next(data)

high = []
low = []
for row in data:
    if int(row[0].split('-')[0]) >= 1983:
        if (row[3] != '') & (row[-1] != ''):
            if (row[0].split('-')[1] == '10') & (row[0].split('-')[2] == '02'):
                high.append(float(row[-1]))
                low.append(float(row[3]))
            
print(high)

print(low)

plt.figure(figsize=(20,5))

plt.plot(high, color='r', ls='--', label='high')
plt.plot(low, color='blue', ls = ':', label='low')

plt.title('1983년이후 내 생일의 기온 그래프')
plt.ylabel('temp')
plt.legend(fontsize=15)

plt.rc('font', family='Malgun Gothic')
plt.show()

### 히스토그램 연습을 해보자

import random

dice=[]

for i in range (10000):
    a = random.randint(1,6)
    dice.append(a)
    
plt.hist(dice, bins=6)
plt.show()

import csv

f = open('C:/Users/victo/OneDrive - 강원대학교/허룡이의 코딩생활/데이터분석 스터디/불러오기 자료/seoul.csv')

data = csv.reader(f)

next(data)

high=[]

for row in data:
    if row[-1] != '':
        high.append(float(row[-1]))
    
print(high)

plt.hist(high, bins=100, color='red')
plt.title('기온 히스토그램 그래프')
plt.rcParams['axes.unicode_minus'] = 'False'
plt.show()

#### 8월의 데이터만 뽑아서 히스토그램을 그려보자

import csv

f = open('C:/Users/victo/OneDrive - 강원대학교/허룡이의 코딩생활/데이터분석 스터디/불러오기 자료/seoul.csv')

data = csv.reader(f)

next(data)

Aug_high=[]

for row in data:
    if (row[0].split('-'))[1] == '08':
        if row[-1] != '':
            Aug_high.append(float(row[-1]))
            
plt.hist(Aug_high, bins=30, color='r')
plt.title('8월의 기온 분포')
plt.show()

#### 1월과 8월의 최고기온 분포를 히스토그램으로 표현해보자

import csv


f = open('C:/Users/victo/OneDrive - 강원대학교/허룡이의 코딩생활/데이터분석 스터디/불러오기 자료/seoul.csv')

data = csv.reader(f)

next(data)

Aug_high=[]
Jan_high=[]

for row in data:
    if (row[0].split('-'))[1] == '08':
        if row[-1] != '':
            Aug_high.append(float(row[-1]))
            
    if (row[0].split('-'))[1] == '01':
        if row[-1] != '':
            Jan_high.append(float(row[-1]))
            
plt.figure(figsize=(10,5))
plt.hist(Aug_high, bins=30, color='r')
plt.hist(Jan_high, bins=30, color='b')
plt.show()

plt.figure(figsize=(10,5))
plt.boxplot([Aug_high, Jan_high])
plt.show()

### Box plot을 그려보자 Boxplot은 데이터의 분포 범위를 확인하기 좋다

import random

data = []

for i in range(100):
    add = random.randint(1,1000)
    data.append(add)
    
plt.boxplot(data)
plt.show()

### 월별 최고기온 데이터를 수집해서 boxplot으로 그려보자

import csv

f = open('C:/Users/victo/OneDrive - 강원대학교/허룡이의 코딩생활/데이터분석 스터디/불러오기 자료/seoul.csv')

data = csv.reader(f)

next(data)

# Jan=[]
# Feb=[]
# Mar=[]
# Apr=[]
# May=[]
# Jun=[]
# Jul=[]
# Aug=[]
# Sep=[]
# Oct=[]
# Nov=[]
# Dec=[]

month=[[],[],[],[],[],[],[],[],[],[],[],[]]

for row in data:
    if row[-1] !='':
        if (row[0].split('-'))[1] == '01':
            month[0].append(float(row[-1]))
        elif (row[0].split('-'))[1] == '02':
            month[1].append(float(row[-1]))
        elif (row[0].split('-'))[1] == '03':
            month[2].append(float(row[-1]))
        elif (row[0].split('-'))[1] == '04':
            month[3].append(float(row[-1]))
        elif (row[0].split('-'))[1] == '05':
            month[4].append(float(row[-1]))
        elif (row[0].split('-'))[1] == '06':
            month[5].append(float(row[-1]))
        elif (row[0].split('-'))[1] == '07':
            month[6].append(float(row[-1]))
        elif (row[0].split('-'))[1] == '08':
            month[7].append(float(row[-1]))
        elif (row[0].split('-'))[1] == '09':
            month[8].append(float(row[-1]))
        elif (row[0].split('-'))[1] == '10':
            month[9].append(float(row[-1]))
        elif (row[0].split('-'))[1] == '11':
            month[10].append(float(row[-1]))
        elif (row[0].split('-'))[1] == '12':
            month[11].append(float(row[-1]))
        else:
            pass

plt.boxplot(month)
plt.show()

### 추가문제 평균기온이 상승하는 그래프를 표현해보기

- 해별로 groupby?

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/victo/OneDrive - 강원대학교/허룡이의 코딩생활/데이터분석 스터디/불러오기 자료/seoul.csv', header=0, encoding='cp949')
# pandas.read_csv함수로 csv파일을 불러와서 data변수에 저장

df = pd.DataFrame(data)
# table형태로 볼 수 있도록 DataFrame함수에 data를 input해서 df변수에 table을 저장

df.columns=['날짜','지점','평균기온','최저기온','최고기온']
# .columns함수를 이용해 table의 열이름을 새로 지정

df['날짜'] = pd.to_datetime(df['날짜'])
# 날짜 데이터는 편하게 다루기 위해서 pandas에서 지원하는 datetime type으로 변환시키자
# 여기서 df['날짜']는 데이터프레임의 날짜 열을 의미한다.

display(df)
df.info()
# 데이터프레임의 각종 정보를 확인하는 info()

date = df['날짜']
date

df['year'] = df['날짜'].dt.year
# df.dt.year 함수를 이용하면 datetime type의 열에서 year만 따로 뽑아낼 수 있다
df['month'] = df['날짜'].dt.month
# df.dt.month 함수를 이용하면 datetime type의 열에서 month만 따로 뽑아낼 수 있다.
display(df)

mask1 = df[df['year'] == 1907].index
mask2 = df[df['year'] == 2019].index
# 1907년과 2019년의 데이터는 1년치 데이터가 아니기 때문에 통계가 의미가 없기에 제외한다.
# 이게 아닐텐데... 한줄에 1907과 2019 모두 masking하는 방법이 없나..?

# mask = df[(df['year']==1907) | (df['year']==2019)]
# 이렇게 코딩하면 두 조건을 동시에 만족하게된다.

df = df.drop(index=mask1)
df = df.drop(index=mask2)
# df에서 1907년과 2019년의 data를 drop(버림)
display(df)

df.set_index(np.arange(0,len(df)), inplace=True)
# 근데 위의 table을 보면 index가 0부터 시작하지 않고 92부터 시작하는데 굉장히 불편하니 index를 새로 설정해주자
# df.set_index함수와 np.arange 함수를 이용한다. numpy.arnage(1,10) = 1부터 10까지의 배열을 생성 [1,2,3....,8,9,10]

display(df)

##### 평균 기온이 ''(공백)인 row는 drop하자

df.isnull().sum()
# 기온의 기록이 되어있지 않은 부분을 확인하기 위해서 isnull() 함수를 이용하자
# 추가로 뒤에 .sum()을 붙여주면 몇개의 null값이 있는지 확인해준다.

df.dropna(how='any', inplace=True)
# dropna 함수는 null값이 있는 행을 모두 날려버리는 함수 null값이 있으면 데이터 처리에 어려움이 있으므로 모두 날려준다
# how='any'는 널값이 있는 모든(any) 행을 날려달라는 의미임

display(df)

df.isnull().sum()
# null값을 날리고 난 뒤 다시 isnull().sum() 해보니 null값이 모두 없어진것을 확인할 수 있다.

#### year column을 이용해서 해당 연도의 평균기온의 mean값을 구하자

grouped_temp = df['평균기온'].groupby(df['year']) 
# 데이터프레임의 평균기온을 연도별로 groupby하자 연도별로 데이터가 묶여서 grouped_temp에 저장된다.

grouped_temp.size() 
# 각 그룹에 속한 sample 수 1년은 365일이고 4년마다 윤달이랑 측정오류 + 뭐시기랑 해서 364~366사이가 있는듯

mean = grouped_temp.mean()
# mean 변수에 각 그룹별 온도의 평균값을 저장하자

# mean을 이용해서 일단 plot을 그려보자 
plt.figure(figsize=(10,5))
plt.plot(mean)
plt.show()

plot을 그렸는데 1950년도쪽에서 뭔가 이상한 데이터가 있다 확인해보자, 아마도 한국전쟁당시인 1950~1953년 데이터가 유력해보인다

df_temp = df[(df['year']==1950) | (df['year']==1951) | (df['year']==1952)]
# 1950, 51, 52년의 데이터만 따로 담아놓은 df_temp을 만들자

pd.set_option('display.max_rows', 250)
# 이건 display했을 때, 250개까지 보여달라는 옵션

display(df_temp)
# 1951년과 1952년의 데이터가 없음 df에서 51년과 52년은 완전히 drop하자

display(df[df['year']==1953]) 
# 확인해보니 1953년 데이터도 12월밖에 없다. 당연히 통계가 제대로 될리가 없다. drop하자
# 아까 그린 plot에서 0도쪽으로 곤두박질 친 데이터가 1953년 12월 데이터의 평균이라 0도에 곤두박질친 것이었음을 예상해볼 수 있다.

del_idx = df[df['year'] == 1953].index
# del_idx에 1953년의 index를 저장하고

df = df.drop(index=del_idx)
# df에서 index가 del_idx(1953년의 index)인 행을 모두 drop한다.
display(df)

#### 이제 데이터가 공백이거나 부족한 부분의 전처리가 완료되었다, 다시 df를 plot으로 그려보자

- 먼저 다시 groupby 함수를 이용해서 year로 groupby하자

grouped_year = df['평균기온'].groupby(df['year']) 
#year 열로 그룹화하고

mean = grouped_year.mean() 
#mean 변수에 각 그룹의 평균값을 저장

print(mean) 
# mean변수의 값 확인
# 각 연도별 평균값이 확인된다.

plt.figure(figsize=(10,6))
plt.plot(mean, color='r')
plt.title('평균 기온 변화 그래프')
plt.xlabel('연도')
plt.ylabel('연평균 기온')

plt.annotate('',
            xy=(2015,13.7),
            xytext=(1910,11.5),
            xycoords='data',
            arrowprops=dict(arrowstyle='->', color='skyblue', lw=3))

plt.annotate('평균기온 증가(1907-2018)',
            xy=(1935,12.3),
            rotation=18,
            fontsize=20)
plt.show()

### 플롯 완성

