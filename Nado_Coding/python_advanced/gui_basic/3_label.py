from tkinter import *

root = Tk()
root.title = ("GUI")
root.geometry("640x480")

label1 = Label(root, text = "hello")
label1.pack()

photo = PhotoImage(file = "/Users/lofichill/Desktop/python/study/\
nado coding/applied python/gui_basic/check.png")
photo2 = PhotoImage(file = "/Users/lofichill/Desktop/python/study/\
nado coding/applied python/gui_basic/no.png") 
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text = "see you again")
    # garbage collector 한테 함수 change가 끝나도 photo2를 지우지 않게 전역변수 설정
    # 왜인지는 모르겠는데 적용안됨..
    # 전역변수로는 안됐는데 아예 밖에서 photo2를 설정하니까 작동함 
    label2.config(image = photo2)


btn = Button(root, text = "click", command = change)
btn.pack()


root.mainloop()