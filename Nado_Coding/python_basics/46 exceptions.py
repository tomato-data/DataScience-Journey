try:
    print("for division only")
    nums = []
    nums.append(int(input("enter first number: ")))
    nums.append(int(input("enter second number: ")))
    # nums.append(int(nums[0]/int(nums[1])))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError:
    print("error! wrong value input")

# error 구문을 그대로 써줌
except ZeroDivisionError as err:
    print(err)

# 따로 지정하지 않은 에러는 이런식으로 처리 가능
except Exception as err:
    print("unidentified error has occurred")
    print(err)