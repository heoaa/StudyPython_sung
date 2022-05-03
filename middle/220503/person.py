# 모든 객체는 속성과 행위(함수)를 담고 있음
# 사람객채를 위한 클래스 Person
from unicodedata import name


print('\n--------------------------------------')

# if a == 13:
#     pass  # 오류 없이 실행가능

class Person :
    __name = ''     # 이름속성
    age = 0       # 나이속성
    height = 100  # 키
    weight = 30   # 몸무게

    # 생성자 재정의
    # 첫번째 매개변수는 반드시 self를 지정해야 함
    def __init__(self,name = None) -> None :     #  -> None 리턴값이 없음
        if name == None :
            self.__name = '허아현'
        else :
            self.__name = name

        print(f'{self.__name}탄생!!')

    # 매직메서드 __str__ 사용 재정의
    def __str__(self) -> str:      #  -> str 문자열로 리턴
        value = f'''객체 {self.__name}\n
        나이 : {self.age}
        키 : {self.height}'''
        return value

    def walk(self, speed):
        print(f'{self.__name}이(가) {speed}km/h로 걷는다.')
        return

    def run(self, speed) :
        print(f'{self.__name}이(가) {speed}km/h로 뛴다.')


# 객체 생성  # __init__ 재정의 후 객체에 이름을 넣으면 생성 가능
# 클래스는 특정 개념을 표현만 할뿐 사용하려면 인스턴스(객체)를 생성해야 함
p = Person('허아현')    
# p.__name = '허아현'
p.age = 25
p.height = 157
p.weight =52

p.walk(2)
p.run(10)

print(type(p))     # <class '__main__.Person'> 

print('\n--------------------------------------')

print(p)    # <__main__.Person object at 0x000001DF701A8FD0>



## 객체 생성 후 속성 변경을 원하지 않는 경우 __를 사용하여 변수 지정
#  클래스 안에서만 접근할 수 있는 속성(비공개속성)