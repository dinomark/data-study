import csv

max_temp = -999
max_date = ''
f = open('Pycharm/seoul.csv')
data = csv.reader(f)
header = next(data)

for row in data:
    if row[-1] == '':
        row[-1] = -999
    row[-1] = float(row[-1])
    if max_temp < row[-1]:
        max_date = row[0]
        max_temp = row[-1]

f.close()
print("최고온도가 가장 높은 날은", max_date + " 그 날의 온도는", max_temp)
