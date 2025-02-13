# 예외처리 구문에서 문제없이 진행되던 예외처리로 넘어가던 무조건 실행되는 구문
# 예외처리하지 않은 것도 에러는 뜨지만 finally는 실행이 됨

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("one digit division only")
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("input: {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, num1/num2))

except ValueError:
    print("wrong value input")

except BigNumberError as err:
    print("error occurred, input one digit only")
    print(err)

finally:
    print("Thank you for using")