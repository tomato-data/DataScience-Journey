from random import *

droven = 0
for customer in range(1, 51):
    driving_time = randrange(5, 51)
    my_option = range(5, 16)

    if driving_time in my_option:
        possibility = "O"
        droven += 1
    else:
        possibility = " "

    print("[{0}] {1}th customer (driving time: {2})" .format(possibility, customer, driving_time))

print("total customers matched: {0}" .format(droven))