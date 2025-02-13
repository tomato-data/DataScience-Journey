class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} has spawned".format(self.name))
        print("hp {0}, damage {1}".format(self.hp, self.damage)) 

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    # attack 과 damaged 가 메소드
    def attack(self, location):
        print("{0} : attacking {1} 'o clock [damage {2}]"\
            # location 은 attack 함수가 받는 인자를 그대로 씀
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : damaged [{1}]".format(self.name, damage))
        self.hp -= damage
        print("{0} : current hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : destroyed".format(self.name))

firebat1 = AttackUnit("firebat", 50, 16)
firebat1.attack(5)

firebat1.damaged(25)
firebat1.damaged(25)