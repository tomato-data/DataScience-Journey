import math
 
class Circle:
    def __init__(self, radius):
        # private variable = 함수 밖에서 호출 못함
        self.__radius = radius

    def get_circumstance(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    # decorator를 이용한 게터와 세터 선언
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("positive numbers only")
        self.__radius = value

circle = Circle(10)
print(circle.radius)
circle.radius = 2
print(circle.radius)


print(circle.get_circumstance())
print(circle.get_area())