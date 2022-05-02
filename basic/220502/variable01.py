# 주석입니다. (프로그래밍에 영향 X)

# 변수
a = '안녕하세요'   # "안녕하세요"
print(a)

a = True
print(a)

a=3.14
print(a)

a=1/10
print(a)

print('값은', a, '입니다')  # 출력 방식 2  ,로 구분하며 갯수는 상관X


# leftvalue에 오른쪽 값을 할당
a=3         # 정수
b=3.141592  # 실수
c='python'  # 문자
d=(1,2,3)   # 튜플은 수정, 삭제가 불가능
e=[4,5,6]   # list는 수정, 삭제가 가능
f=[7,'8',True]  
g=False     # bool 값은 True = 1, False = 0의 값을 가짐
print('각 변수의 값', 'a=', a, 'b=', b, 'c=', c, 'd=', d)
print('각 변수의 값', 'e=', e, 'f=', f, 'g=', g)

# 변수명 지정 : 숫자로 시작할 수 없고, 특수문자는 _만 가능
# SyntaxError
Var5 = 5
var5 = '8'
print(Var5, var5)

# 메모리 id 
print(id(a))
print(id(b))
print(id(c))