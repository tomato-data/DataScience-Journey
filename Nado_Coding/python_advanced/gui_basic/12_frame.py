from tkinter import *

root = Tk()
root.title = ("GUI")
root.geometry("640x480")

Label(root, text = "choose menu").pack(side = TOP)

Button(root, text = "make order").pack(side = BOTTOM)
# menu
frame_burger = Frame(root, relief = "solid", bd = 1)
frame_burger.pack(side = "left", fill = "both", expand = True)


Button(frame_burger, text = "hamburger").pack()
Button(frame_burger, text = "cheeseburger").pack()
Button(frame_burger, text = "chickenburger").pack()

# drinks
frame_drink =  LabelFrame(root, text = "drinks")
frame_drink.pack(side = "right", fill = "both", expand = True)

Button(frame_drink, text = "coke").pack()
Button(frame_drink, text = "cider").pack()

root.mainloop() 