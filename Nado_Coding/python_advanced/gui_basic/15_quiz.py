# 메모장 앱 만들기

from tkinter import *
import os

root = Tk()
root.title = ("no title - Windows memo")
root.geometry("640x480")

filename = "my_text.txt"

def open_file():
    # filename이 있으면
    if os.path.isfile(filename):
        with open(filename, "r", encoding = "utf8") as file:
            txt.delete("1.0", END) # text 위젯 초기화
            txt.insert(END, file.read()) # 파일 내용 본문에 입력

def save_file():
    with open(filename, "w", encoding = "utf8") as file:
        file.write(txt.get("1.0", END))

menu = Menu(root)

menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = "Open File", command = open_file)
menu_file.add_command(label = "Save", command = save_file)
menu_file.add_separator() 
menu_file.add_command(label = "Exit", command = root.quit) 
menu.add_cascade(label = "File", menu = menu_file)

# 왜인지 이부분 적용 안됨
menu.add_cascade(label = "Edit") 
menu.add_cascade(label = "Template")
menu.add_cascade(label = "View")
menu.add_cascade(label = "Help")

root.config(menu = menu)

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

txt = Text(root, yscrollcommand = scrollbar.set)
# 전체 공간 꽉 채우기
txt.pack(side = LEFT, fill = BOTH, expand = True)

scrollbar.config(command = txt.yview)

frame_txt = Frame(root, relief = SOLID)
frame_txt.pack(fill = BOTH, expand = True)


scrollbar.config(command = txt.yview)

root.mainloop()