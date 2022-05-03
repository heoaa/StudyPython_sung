# # class 복습 (파이썬 코딩 도장)
# # print('\n--------------------------------------')

# # '''
# # class 클래스이름
# #     def 메서드(self)
# #         코드
# # '''

# # class Person :
# #     def greeting(self) :
# #         print('Hello')


# # # 클래스는 특정 개념을 표현만 할뿐 사용하려면 인스턴스(객체)를 생성해야 함
# # print('\n--------------------------------------')

# # ''' 인스턴스 = 클래스() '''

# # james = Person()


# # # 메서드는 인스턴스를 통해 호출
# # print('\n--------------------------------------')

# # ''' 인스턴스.메서드() '''

# # james.greeting()

# #  클래스에 속성을 만들 땐 __init__ 메서드 안에 self.속성에 값을 할당
# print('\n--------------------------------------')

# ''' 
# class 클래스이름 :
#     def __init__(self)
#         self.속성 = 값
# '''

# class Person :
#     def __init__(self) :
#         self.hello = '안녕하세요.'

#     def greeting(self) :
#         print(self.hello)

# james = Person()
# james.greeting()


# 연습문제 p508
# 다음 소스코드에서 클래스를 작성하여 게임 캐릭터의 능력치화 '베기'가 출력되게 만드세요.
from zoneinfo import available_timezones


print('\n--------------------------------------')

# 정답
class Knight :
    def __init__(self, health, mana, armor) :
        self.health = health
        self.mana = mana
        self.armor = ArithmeticError
    
    def slash(self) :
        print('베기')

# 소스코드
x=Knight(health = 542.4, mana = 210.3, armor = 38)
print(x.health, x.mana, x.armor)
x.slash()


# # 심사문제 p509
# # 
# print('\n--------------------------------------')


# class Annie :
#     def __init__(self, helth, mana, ability_power) :
#         self.health = input(health)




# # 소스코드
# health, mana, ability_power = map(float, input().split())
# x = Annie(heath = health, mana=mana, ability_power=ability_power)
# x.tibbers()