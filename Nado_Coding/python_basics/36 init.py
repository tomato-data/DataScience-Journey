# 생성자, 유닛을 만들 때 '자동으로' 호출되는 부분
# marine, tank 같이 클래스로 만들어지는 것을 객체, unit 클래스의 instance라고 함
# class를 만들 때 __init__ 없이 하면 어떻게 되는가? 없이 만들 수는 있는가?

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} has spawned".format(self.name))
        print("hp {0}, damage {1}".format(self.hp, self.damage))

marine = Unit("marine", 40, 5)
marine2 = Unit("marine", 40, 5)
tank = Unit("tank", 150, 35)