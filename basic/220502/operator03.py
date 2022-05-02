# 문자열 포맷팅
name = 'heo'
login_str = '{0}님 로그인 중'.format(name)

print(login_str)


print('{0}, {1}, {2}'.format('하나', 2, login_str))
print(f"{'하나'}, {2}, {login_str}")   # 위 코드와 결과 동일

print('\n--------------------------------------')

# 소수점 표현
PI = 3.14159268
print('{0:0.2f}'.format(PI))
print(f'{PI:0.3f}')

print('\n--------------------------------------')

full_name = 'Heo A Hyun'
sp_names = full_name.split()   # 문자열을 ' '로 잘라서 리스트로 저장
print(sp_names)
print(sp_names[0])

print('\n--------------------------------------')

greeting = 'Hello, World'
words =greeting.split(',')     # 문자열을 ,로 잘라서 리스트로 저장
print(words)
print(words[1].strip())        # , 이후 공백 제거

print('\n--------------------------------------') 

hi = '            Hello~      .'
print(hi.lstrip())      # oracle LTRIM() 동일
print(hi.rstrip())      # RTRIM
print(hi.strip())       # TRIM

print('\n--------------------------------------') 

# 문자열 특정 단어, 문자열 값 변경
print(full_name.replace('Heo A', "H A"))

print('\n--------------------------------------') 

# 리스트 연산
arr = ['1', 2, 3, '4', 5]

print(arr[1] + arr[2])      # 2 + 3
print(arr[3] * arr[2])      # '4' 글자를 3번 반복 출력
print(arr[3] + arr[0])      # '4' 글자와 '1' 글자를 합쳐라
# print(arr[0] + arr[1])    # 자료형이 다른 경우 연산 불가능

print('\n--------------------------------------')

# 이중 리스트
arr2 = [1, 2, 3.14, ['Hi', 'My', 'Friends']]
print(arr2[2])
print(arr2[3][1])    # MY
print(arr2[3][1][0]) # M

print('\n--------------------------------------')

arr3 = arr + arr2
print(arr3)
