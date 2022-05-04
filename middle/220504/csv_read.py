#  csv파일 읽기
print('\n--------------------------------------')
import csv

file_name = './busanbus_220504.csv'

# 보통 노트패드에서 utf-8로 변경 후 작업
f = open(file_name, mode='r', encoding='utf-8')

reader = csv.reader(f, delimiter = ',')     # 구분자가 ,인 경우
next(reader)   # 첫 행이 제목줄(헤더)인 경우 읽지않음

for line in reader :
    print(line)

f.close()     ## 필수