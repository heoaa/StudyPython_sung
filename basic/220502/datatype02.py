## 문자열
# \n : 줄바꿈(탈출문자)
# \t : tab
from distutils.spawn import spawn


bruce_eckel = ' Life is short. \n You need \tPython.'
print(bruce_eckel)

# 여러줄 문자열
multi_line = '''Life is short.
You need Python.
And I need C#, too.
'''
print(multi_line)

print('\n--------------------------------------')

## 불형
print(1 + 1 == 1)
print(bool(1))
print(bool(0))

print('\n--------------------------------------')

## 리스트(배열)
b = [1, 2, 3, 4]
print(b)

# append(값) : 리스트 마지막에 해당 값을 추가
b.append(5)
print(b)

# insert(위치, 값) : 원하는 위치(인덱스)에 값 추가
b.insert(3, 10)
print(b)

b.sort()     # 오름차순 정렬
print(b)

b.reverse()  # 내림차순 정렬
print(b)

b.remove(10) # 원소 삭제
print(b)

print(type(b))

print(b[2])

print('\n--------------------------------------')

## 튜플
# c.append(5) : 튜플은 추가, 수정, 삭제가 불가능하므로 에러 발생
c = (1, 2, 3, 4)
print(c)

print(c[2])

print('\n--------------------------------------')

## 딕셔너리 : key:value의 쌍
#spiderman ={   'name' : '피터 파커', 
#    'age' : 18,
#    'weapon' : '웹슈터'
#    'memberOfAvengers' : True }

#print(spiderman)
#print(spiderman['name'])

#print(spiderman[2])

# set 집합 : 자료 중복 제거로도 활용

