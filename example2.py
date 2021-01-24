import csv

f = open('Pycharm/seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data:
    # 누락된 데이터가 있으므로, 오류가 발생한다.
    # 최고 기온이 적혀 있는 테이블로, str -> float형태로 바꾼다.
    row[-1] = float(row[-1])
    print(row)
f.close()

'''
    이 코드에서는 오류가 발생한다.
'''
