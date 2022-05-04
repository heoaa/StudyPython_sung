#  파일 입출력 1 - 쓰기

# w : 없으면 생성, 있으면 삭제 후 재생성(새로쓰기)
# a : 기존 파일을 열어 추가(추가쓰기)

f = open('C:/STUDY/StudyPython_sung/temp.txt', mode='w', encoding='utf-8')

f.write('안녕하세요.\n')
f.write('저는 허아현입니다.\n')
f.write('한국사람이죠.\n')

# 필수 (파일, 데이터베이스, 네트워크는 연결 후 반드시 클로징 필요)
f.close()     

print('파일 생성 완료')