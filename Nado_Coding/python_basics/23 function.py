#   전달값과 반환값

def open_account():
    print("new account has been approved")

open_account()

def deposit(balance, amount):
    print("deposit complete, {} left in balance" \
        .format(balance + amount))
    return balance + amount

def withdraw(balance, amount):
    if balance >= amount:
        print("withrawl complete, balance left: {0}" \
            .format(balance - amount))
        return balance - amount
    else:
        print("tried pull {0}. withdrawl failed, balace left: {1}" \
            .format(amount, balance))
        return balance

def withdraw_night(balance, amount):
    commission = 100
    return commission, balance - amount - commission 
    # return 에 튜플 형식으로 두개 이상의 값을 보내줄 수 있음
balance = 0
balance = deposit(balance, 1000)
print(balance) 
# return 으로 반환 된 값을 balance 변수에 저장, return이 없으면 none을 반환

# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("commission fee: {0},  balance left: {1}" .format(commission, balance))