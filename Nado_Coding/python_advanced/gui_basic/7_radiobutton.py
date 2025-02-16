from tkinter import *

root = Tk()
root.title = ("GUI")
root.geometry("640x480")

Label(root, text = "select the menu").pack()

# radio는 하나씩 선택, 복수 선택 불가
burger_var = IntVar() # int 형으로 값을 저장
btn_burger1 = Radiobutton(root, text = "hamburger", value = 1, variable = burger_var)
# 기본 1 선택 
btn_burger1.select()
btn_burger2 = Radiobutton(root, text = "cheeseburger", value = 2, variable = burger_var)
btn_burger3 = Radiobutton(root, text = "chickenburger", value = 3, variable = burger_var)

btn_burger1.pack() 
btn_burger2.pack()
btn_burger3.pack()

Label(root, text = "select your drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text = "coke", value = "콜라", variable = drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text = "cider", value = "사이다", variable = drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get()) # 선택된 라디오의 값(value)을 가져옴
    print(drink_var.get()) # 선택된 음료 값 출력

btn = Button(root, text = "order", command = btncmd)
btn.pack()

root.mainloop() 