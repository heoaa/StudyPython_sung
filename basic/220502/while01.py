# while문 : 조건문이 True인 동안 계속해서 수행문 반복
print('\n--------------------------------------')

hit = 0

while (hit < 100) :
    hit += 1

    print(f'나무를 {hit}번 찍었습니다.')
    if hit == 10 : 
        print('나무가 넘어갑니다!!')
        break
    else :
        print('나무가 아직 안넘어갔네요.\n')

print('나무찍기 완료!!')