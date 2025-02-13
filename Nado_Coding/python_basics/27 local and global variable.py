gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun을 사용
    gun = gun - soldiers
    print("inside the function, gun left is {0}".format(gun))

# 인자에 있는 gun도 지역변수 취급, 함수 밖에 gun에는 상호작용 없음
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("inside the function, gun left is {0}".format(gun))
    return gun

print("all guns {}".format(gun))

# checkpoint(2)
# 밖에있는 gun을 활용해서 return 값으로 바꾸는 법 
gun = checkpoint_ret(gun, 2)

print("guns left {}".format(gun))


# gun 이란 함수는 할당도 안됐는데 사용이 되었다
# gun = gun - soldiers 에서 우측변에 있는 gun은 밖에 있는 gun이랑은 상관이 없음
# 지역변수를 함수 밖에서  따로 호출 할 수 있는지?
# global은 많이 쓸 수록 코드 관리가 어려워지기 때문에 다른 방법이 선호 됨