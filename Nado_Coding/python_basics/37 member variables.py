# self. --- = 멤버 변수

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} has spawned".format(self.name))
        print("hp {0}, damage {1}".format(self.hp, self.damage))

wraith1 = Unit("wraith", 80, 5)

print("unit name: {0}, damage {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("wraith", 80, 5)
wraith2.clocking = True

# clocking 은 class 내에 없음
# 객체에 외부에서 추가로 변수를 만들어 쓸 수가 있음
# 이 경우, wraith2 에는 clocking이 생겼지만 wraith1 에는 적용 안 됨

if wraith2.clocking == True:
    print("{0} is currently clocking".format(wraith2.name))