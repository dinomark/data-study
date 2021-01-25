# csv파일을 불러오기 위한 라이브러리 import
import csv

# seoul.csv파일을 열어서 f라는 변수에 저장
f = open("Pycharm/seoul.csv", 'r', encoding='utf-8')

# f라는 파일을 csv 파일의 reader라는 함수를 이용하여 불러옴
datas = csv.reader(f)

# 데이터를 한줄 한줄 읽어오면서 출력
for data in datas:
    print(data)

# 파일을 닫음
f.close()