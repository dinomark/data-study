import csv

f = open('Pycharm/seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data:
    # 데이터의 마지막란(최고기온)이 공란이라면?
    if row[-1] == '':
        # -999라는 숫자를 넣는다.
        row[-1] = -999
    # str -> float 형으로 형변환한다.
    row[-1] = float(row[-1])
    print(row)
f.close()

'''
    이 코드에서는 오류가 발생하지 않는다.
'''
