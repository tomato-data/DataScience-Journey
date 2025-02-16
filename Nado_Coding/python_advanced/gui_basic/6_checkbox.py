from tkinter import *

root = Tk()
root.title = ("GUI")
root.geometry("640x480")

chkvar = IntVar() #chkvar 에 int 형으로 저장
chkbox = Checkbutton(root, text = "don't show for today", variable = chkvar)
# chkbox.select() # 자동 선택 처리
# chkbox.deselect() # default = deselect이지만 위쪽에서 선택했다하면 deselect 가능
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = "don't show for a week", variable = chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get()) # 0 일 때는 해제 1 일 때는 체크
    print(chkvar2.get( ))


btn = Button(root, text = "click", command = btncmd)
btn.pack()

root.mainloop() 