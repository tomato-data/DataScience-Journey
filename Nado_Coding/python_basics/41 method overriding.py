# 부모클래스에서 정의한 메소드말고 자식클래스에서 정의한 메소드를 사용하고 싶을 때 
# 메소드를 새롭게 정의해서 사용 하는 것 = 오버라이딩

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[nonflyable unit movement] ")
        print("{0} : moving to {1} 'o clock [speed : {2}]"\
            .format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : attacking {1} 'o clock [damage {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : damaged [{1}]".format(self.name, damage))
        self.hp -= damage
        print("{0} : current hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : destroyed".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : flying to {1} 'o clock [speed : {2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0 처리
        Flyable.__init__(self, flying_speed) 

    def move(self, location):
        print("[flyable unit movement]")
        self.fly(self.name, location)

vulture1 = AttackUnit("vulture", 80, 10, 20)
battlecruiser1 = FlyableAttackUnit("battlecruiser", 500, 25, 3)

# 지상인지 공중인지 확인해야함 = 귀찮음
# 오버라이딩으로 고쳐보기
# FlyableAttackUnit 에서 move()를 재정의 했기 때문에
# Unit의 move()가 아닌 FlyableAttackUnit의 move()를 사용
vulture1.move(11)
battlecruiser1.move(5)