# for문
print('\n--------------------------------------')

#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0

for x in range(1, 101) : 
    result = result + x

print('배열의 합은', result)

print('\n--------------------------------------')

arr2 = ('me', 'my', 'friend', 'jane')

for item in arr2 :
    #print(f'{item:>10}')     # 전체길이를 10자리 맞추어 출력
    print(f'{item * 2}')


## 1~10까지 수에서 짝수 구분하기`
print('\n--------------------------------------')

for num in range(2, 11, 2) :
    print(f'{num}는 짝수입니다.')

print('\n--------------------------------------')

for num in range(1,11, 2) :
    if num % 2 == 0 :
        print(f'{num}는 짝수입니다.')
    else :
        print(f'{num}는 홀수입니다.')


## for문 내에서 사용하는 continue, break
print('\n--------------------------------------')

values = [1, 3, 5, 7, 9, 11, 13, 15, 17 ,19]
num=0

for item in values :
    num += 1     # num = num + 1 과 동일
    if (num % 2) == 0 :
        #break    # 반복문 탈출
        continue  # if 조건만 패스하고 다음 값 진행
    else :
        print(f'{num}번 수는 {item}입니다.')