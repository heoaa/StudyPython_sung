# 파일 입출력 2 - 읽기
print('\n--------------------------------------')

f=open('./temp.txt', mode='r', encoding='utf-8')

# t = f.read()     # 보통 한번에 잘 안불러옴

while True :                # 무한루프
    line = f.readline()     # 한 줄씩 읽기
    if not line : break

    print(line, end = '')

# print(t)

f.close()    # 필수
print('파일 읽기 완료')