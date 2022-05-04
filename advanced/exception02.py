# 예외처리 2 - 예외발생 2
print('\n--------------------------------------')

x, y = map(int, input('두 수를 입력하세요 > ').split(' '))
z = 0
print(f'x = {x}')
print(f'y = {y}')


try : 
    z = x / y
    print(f'{x} / {y} = {z}')
# except TypeError as e :
#     print('형변환 하세요.')
# except ZeroDivisionError as e :
#     print('두번째수에 0은 넣지마세요.')
except Exception as e :      # 모든 에러의 부모형
    print(f'예외발생 {e}')

# finally에는 각종 close 함수를 넣어 클로징 등 활용

print('나누기 종료')