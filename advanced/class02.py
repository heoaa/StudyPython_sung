# 클래스 상속
class Vehicle :
    name = '탈것'
    color = '색상'
    
    def __init__(self, color = None) -> None:
        self.color = color
        print(f'{self.color}색 {self.name} 생성!')

    def desc(self) :
        print(f'{self.name} 객체')

    def move(self) :
        print(f'{self.name} 이동!')
    
# Vehicle 클래스를 상속받은 Car
class Car(Vehicle) :
    name = '자동차'
    brand = '현대'
    
    def __init__(self, color=None) -> None:
        super().__init__(color)
        print(f'{color}색 {self.brand} {self.name} 생성!!')

    def move(self) :
        super().move()   # 부모가 가진 move 사용하기 위함
        print(f'{self.name} 달린다!')   # 자식이 부모의 속성을 변경하여 사용할 수 있음

    def stop(self) :
        print('브레이크로 멈춤')     # 부모에게 없는 경우 자식이 직접 만들어 사용할 수 있음

if __name__ == '__main__' :
    vcl = Vehicle('검은')
    vcl.desc()
    vcl.move()
    # 부모의 경우 stop이 없음

    mycar = Car('흰')
    mycar.desc()
    mycar.move()
    mycar.stop()
