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

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # 아무것도 안하고 일단 넘어감
        # 일단은 오류 안일으키고 완성된 것 처리
        pass

supply_depot = BuildingUnit("supply depot", 500, 7)

def game_start():
    print("[notice] new game started")

def game_over():
    pass

game_start()
game_over()