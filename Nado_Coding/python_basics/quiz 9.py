class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while True:
    try:
        print("chicken left: [{0}]".format(chicken))
        order = int(input("how many chicken are you ordering? "))
        if order > chicken:
            print("not enough chicken")
        elif order < 1 or type(order) == str:
            raise ValueError
        else:
            print("[waiting no. {0}] {1} chicken(s) order made"\
                .format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError

    except ValueError:
        print("wrong value input")

    except SoldOutError:
        print("sold out")
        break
    
    except Exception as err:
        print(err)