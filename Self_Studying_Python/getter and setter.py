import math
 
class Circle:
    def __init__(self, radius):
        # private variable = 함수 밖에서 호출 못함
        self.__radius = radius

    def get_circumstance(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    # 게터와 세터 선언
    def get_radius(self):
        return self.__radius
    # 예외처리
    def set_radius(self, value):
        if value <= 0:
            raise ValueError("positive numbers only")
        self.__radius == value
    
circle = Circle(10)
print(circle.get_circumstance())
print(circle.get_area())

print(circle.get_radius())
# 세터로 반지름 재설정, 게터를 굳이 앞에 안써줘도 작동함
circle.set_radius(2)
print(circle.get_circumstance())
print(circle.get_area())