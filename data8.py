#%%
import matplotlib.pyplot as plt
plt.hist([1,1,2,3,4,5,6,6,7,8,10])
plt.show()
# %%
import random
print(random.randint(1,6))
# %%
import random
dice = list()

for i in range(5):
    dice.append(random.randint(1,6))

print(dice)
# %%
import matplotlib.pyplot as plt
import random

dice = list()
for i in range(5):
    dice.append(random.randint(1,6))

plt.hist(dice, bins=6)
plt.show()
# %%
import matplotlib.pyplot as plt
import random

dice = list()
for i in range(100):
    dice.append(random.randint(1,6))

plt.hist(dice, bins=6)
plt.show()
# %%
import matplotlib.pyplot as plt
import random

dice = list()
for i in range(1000000):
    dice.append(random.randint(1,6))

plt.hist(dice, bins=6)
plt.show()
# %%
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = list()

for row in data:
    if row[-1] != '':
        result.append(float(row[-1]))

plt.hist(result, bins=100, color='r')
plt.show()
# %%
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
aug = list()

for row in data:
    month = row[0].split('.')[1]
    if row[-1] != '':
        if month == '8':
            aug.append(float(row[-1]))

plt.hist(aug, bins=100, color='b')
plt.show()
# %%
### 1월과 8월의 데이터를 히스토그램으로 시각화하기
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)

aug = list()
jen = list()

for row in data:
    month = row[0].split('.')[1]
    if row[-1] != '':
        if month == '1':
            jen.append(float(row[-1]))
        elif month == '8':
            aug.append(float(row[-1]))
plt.rc("font", family="NanumGothic")
plt.rcParams['axes.unicode_minus'] = False
plt.title("1월과 8월의 최고기온의 분포")
plt.hist(aug, bins=100, color='r')
plt.hist(jen, bins=100, color='b')
plt.show()
# %%
### 랜덤한 데이터를 상자 그림으로 표현하기
import random
import matplotlib.pyplot as plt

result = []

for i in range(13):
    result.append(random.randint(1, 1000))
print(result)

plt.boxplot(result)
plt.show()

# %%
import numpy as np

result = np.array(result)
print("1/4 " + str(np.percentile(result, 25)))
print("2/4 " + str(np.percentile(result, 50)))
print("3/4 " + str(np.percentile(result, 75)))
# %%
### 실제 기온 데이터를 가지고 상자 그림으로 표현하기
import csv
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

f = open('seoul.csv')
data = csv.reader(f)
next(data)

result = []

for row in data:
    if row[-1] != '':
        result.append(float(row[-1]))

plt.rc('font', family='NanumGothic')
plt.boxplot(result)
plt.xlabel("최고기온")
plt.show()
# %%
### 1월과 8월의 상자 그림
import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
jan = []
aug = []

for row in data:
    month = row[0].split('.')[1]
    if row[-1] != '':
        if month == '1':
            jan.append(float(row[-1]))
        elif month == '8':
            aug.append(float(row[-1]))

plt.boxplot(jan)
plt.boxplot(aug)
plt.show()
# %%
plt.boxplot([jan, aug])
plt.show()
# %%
### 월별로 box plot 그리기
import matplotlib.pyplot as plt
import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data)

month = []

for i in range(12):
    month.append([])

for row in data:
    if row[-1] != '':
        month[int(row[0].split('.')[1])-1].append(float(row[-1]))

plt.boxplot(month)
plt.show()

# %%
import matplotlib.pyplot as plt
import csv
plt.style.use('ggplot')

f = open('seoul.csv')
data = csv.reader(f)
next(data)

day = []

for i in range(31):
    day.append([])

for row in data:
    if row[-1] != '':
        if row[0].split('.')[1] == '8':
            day[int(row[0].split('.')[2])-1].append(float(row[-1]))

plt.figure(figsize=(10,5), dpi=300)
plt.boxplot(day, showfliers=False)
plt.rc('font', family='NanumGothic')
plt.title("8월 한달간 온도 분포")
plt.show()