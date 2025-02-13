class Unit:
    def __init__(self):
        print("unit operator")

class Flyable:
    def __init__(self):
        print("flyable operator")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# super는 맨 처음 인자만 init 함수가 호출 된다.
# 여러개를 호출하려면 따로 명시적으로 해줘야 함
dropship = FlyableUnit()