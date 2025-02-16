from tkinter import *

root = Tk()
root.title = ("GUI")
root.geometry("640x480")

txt = Text(root, width = 30, height = 5)
txt.pack()

txt.insert(END, "write something")

# enter로 줄꿈 사용 불가. 로그인 할 때 아이디같은거 받을때 = entry
e = Entry(root, width = 30)
e.pack()
e.insert(0, "only write one line")

def btncmd():
    # 처음부터 끝까지에있는 모든 텍스트를 가져오기
    # line 1, column 0
    print(txt.get("1.0", END))
    # entry는 get만 적어도 됨
    print(e.get())

    txt.delete("1.0", END)
    # insert 할 때 넣은 값 = 0
    e.delete(0, END)


btn = Button(root, text = "click", command = btncmd)
btn.pack()

root.mainloop()