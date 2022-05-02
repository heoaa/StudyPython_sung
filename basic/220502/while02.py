# 무한루프
print('\n--------------------------------------')

num = 0

while True : 
    print('''처리번호를 입력하세요.
1. 회원입력
2. 회원검색
3. 회원수정
4. 회원삭제
5. 종료
번호 입력 : ''')
    num = int(input())    # 키보드로 입력받은 수 num에 할당

    if num == 1 :
        print('회원정보입력')
    elif num == 2 :       # 1은 아니고 2면
        print('회원검색')
    elif num == 3 :       # 1, 2도 아니고 3이면
        print('회원수정')
    elif num == 4 :       # 1, 2, 3도 아니고 4면
        print('회원삭제')
    elif num == 5 :       # 1, 2, 3, 4도 아니고 5라면
        print('프로그램 종료')
        break
    else :
        print('잘못 입력했습니다.')
        continue