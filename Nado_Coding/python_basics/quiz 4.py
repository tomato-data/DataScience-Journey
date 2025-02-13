from random import *

lst = range(1, 21)
lst = list(lst)
# shuffle(lst)
winners = sample(lst, 4)


print("""
--당첨자 발표--
치킨 당첨자: """ + str(winners[0]) + """
커피 당첨자: [""" + str(winners[1:]) + """]
-- 축하합니다 --
""")