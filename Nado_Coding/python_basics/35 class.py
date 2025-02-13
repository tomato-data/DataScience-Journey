# name = "marine"
# hp = 40
# damage = 5

# print("{0} unit has been spawned".format(name))
# print("hp {0}, damage = {1}\n".format(hp, damage))

# tank_name = "tank"
# tank_hp = 150
# tank_damage = 35

# print("{0} unit has been spawned".format(tank_name))
# print("hp {0}, damage = {1}\n".format(tank_hp, tank_damage))

# # 이런 식으로 유닛이 생성 될 때마다 하면 일이 많아지기 때문에 class 필요
# tank2_name = "tank"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} unit has been spawned".format(tank2_name))
# print("hp {0}, damage = {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : attacking {1} 'o clock [damage {2}]"\
#         .format(name, location, damage))

# attack(name, "1", damage)
# attack(tank_name, "2", tank_damage)
# attack(tank2_name, "2", tank2 _damage)

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