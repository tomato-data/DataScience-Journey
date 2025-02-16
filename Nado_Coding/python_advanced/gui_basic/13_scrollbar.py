from tkinter import *

root = Tk()
root.title = ("GUI")
root.geometry("640x480")

# scrollbar 랑 scrollbar 대상이 되는 widget을 하나의 프레임에 넣는게 관리가 편함

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side = RIGHT, fill = Y) # fill y 로 위아래 꽉 채우기

# yscrollcommand set이 없으면 스크롤을 내려도 다시 올라: mapping
listbox = Listbox(frame, selectmode = EXTENDED, height = 10, \
    yscrollcommand = scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, "day " + str(i))
listbox.pack(side = LEFT)

# scrollbar가 상하로 움직이는 목록 처리: mapping
scrollbar.config(command = listbox.yview)

root.mainloop() 