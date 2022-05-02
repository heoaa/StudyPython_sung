# if문   (if 조건문 : 실행문1, 실행문2 ...)
print('\n--------------------------------------')

name = '홍길동'
gender = '남'

if name == '홍길동' and gender == '남' :
    print(name,'님 진료실로 들어갑니다.')
    print('의사쌤한테 인사합니다.')

else :
    if gender == '여' :
        print('성별이 다릅니다.')    
    else :
        print('부를때까지 기다리세요.')
        print(name,'님이 궁시렁거립니다.')


print('\n--------------------------------------')

num = 10

if num != 9 :
    print('9가 아닙니다.')
else :
    print('9입니다.')