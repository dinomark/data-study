#%%
# csv 파일을 읽어오기 위한 라이브러리 선언
import csv
# %%
# csv 파일을 읽어와서 데이터를 한줄씩 출력한다.
f = open("seoul.csv")
data = csv.reader(f)

for row in data:
    print(row)
# %%
#데이터를 읽어와서 맨 윗줄의 헤더를 next로 제외시킨 다음, 최고기온만 출력
f = open('seoul.csv')
data = csv.reader(f)
next(data)

for row in data:
    print(row[-1])
# %%
# 데이터를 리스트에 저장하여 출력한다.
f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = list()

for row in data:
    if row[-1] != '':
        result.append(row[-1])

print(result)
# %%
print(len(result))
# %%
import matplotlib.pyplot as plt

plt.plot(result, 'r')
plt.show()
# %%
f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = list()


for row in data:
    if row[-1] != '':
        if row[0].split('.')[1] == '8':
            result.append(float(row[-1]))

print(result)
plt.plot(result, 'hotpink')
plt.show()
# %%
f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = list()

for row in data:
    if row[-1] != '':
        if row[0].split('.')[1] == '2' and row[0].split('.')[2] == '14':
            result.append(float(row[-1]))

plt.plot(result, 'orange')
plt.show()
# %%
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)

high = list()
low = list()

for row in data:
    # 최고 기온과 최저기온이 공란이 아닐경우
    if row[-1] != '' and row[-2] != '':
        # 첫번째 데이터를 split 하여 int type으로 형변환 시킨 다음, 1983년보다 큰 경우
        if 1983 <= int(row[0].split('.')[0]):
            # 첫번째 데이터를 split하여 해당하는 날짜가 2월 14일일 경우
            if row[0].split('.')[1] == '2' and row[0].split('.')[2] == '14':
                # 최고기온은 high 리스트에 넣고 최저 기온은 low 리스트에 append 한다.
                high.append(float(row[-1]))
                low.append(float(row[-2]))

plt.plot(high, 'r')
plt.plot(low, 'b')
plt.show()
# %%
import csv
import matplotlib

f = open('seoul.csv')
data = csv.reader(f)
next(data)

avg = list()
year = list()

for row in data:
    if row[2] != '':
        if row[0].split('.')[1] == '11' and row[0].split('.')[2] == '3':
            year.append(int(row[0].split('.')[0]))
            avg.append(float(row[2]))

plt.plot(year, avg, 'r')
plt.show()
# %%
import csv
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
### 데이터를 불러와서, 맨 위의 한글 데이터를 제외
f = open('seoul.csv')
data = csv.reader(f)
next(f)

### 최고기온과 최저기온의 변화를 저장할 list 선언
high = list()
low = list()

for row in data:
    if row[-1] != '' and row[-2] != '':
        ### data에서 년도 데이터만 추출하여 data에 저장
        data = row[0].split('.')
        if 1983 <= int(data[0]):
             if data[1] == '11' and data[2] == '3':
                 ### 내 생일의 최고기온 및 최저기온을 선언한 리스트에 저장
                 high.append(float(row[-1]))
                 low.append(float(row[-2]))
plt.rc('font', family='NanumGothic')
plt.rcParams['axes.unicode_minus']=False

plt.title("내 생일의 기온 변화 그래프")
### 최고기온은 hotpink 색으로 출력
plt.plot(high, 'hotpink', label='high')
### 최저기온은 skyblue색으로 표현
plt.plot(low, 'skyblue', label='low')

plt.legend()
plt.show()
# %%
