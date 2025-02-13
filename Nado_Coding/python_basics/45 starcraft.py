from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} has been spawned".format(self.name)) 
        # self.name이나 name 아무거나 써도 됨, 매개변수랑 파라미터로 받았기 때문
 
    def move(self, location):
        print("{0} : moving to {1} 'o clock [speed : {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : damaged [{1}]".format(self.name, damage))
        self.hp -= damage
        print("{0} : current hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : destroyed".format(self.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : attacking {1} 'o clock [damage {2}]"\
            .format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "marine", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : stimpack activated [hp -10]"\
                .format(self.name))
        else:
            print("{0} : not enough hp".format(self.name))

class Tank(AttackUnit):

    seige_developed = False # 시즈모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "tank", 150, 1, 35)
        self.seige_mode = False

    def set_seige_mode(self):
        if Tank.seige_developed == False:
            return
        
        if self.seige_mode == False:
            print("{0} : activating seige mode".format(self.name))
            self.damage *= 2
            self.seige_mode = True

        else:
            print("{0} : disactivating seige mode".format(self.name))
            self.damage /= 2
            self.seige_mode = False


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
        self.fly(self.name, location)


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "wraith", 80, 20, 5)
        self.cloacked = False

    def cloacking(self):
        if self.cloacked == True:
            print("{0} : disactivating cloacking mode".format(self.name))
            self.cloacked == False

        else:
            print("{0} : activating cloacking mode".format(self.name))
            self.cloacked == True


def game_start():
    print("[notice] new game started")

def game_over():
    print("Player : GG")
    print("Player has left the game")

game_start()

M1 = Marine()
M2 = Marine()
M3 = Marine()

T1 = Tank()
T2 = Tank()

W1 = Wraith()

attack_units = []
attack_units.append(M1)
attack_units.append(M2)
attack_units.append(M3)
attack_units.append(T1)
attack_units.append(T2)
attack_units.append(W1)

for unit in attack_units:
    unit.move(1)

Tank.seige_developed = True
print("[notice] seige mode upgrade complete")

for unit in attack_units:
    # 지금 만들어진 객체가 어떤 클래스의 인스턴스인지 확인
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seige_mode()
    elif isinstance(unit, Wraith):
        unit.cloacking()

for unit in attack_units:
    unit.attack(1)


for unit in attack_units:
    unit.damaged(randint(5, 21)) # random damage

game_over()