import tkinter.ttk as ttk
import time
from tkinter import *

root = Tk()
root.title = ("GUI")
root.geometry("640x480")

# indeterminate = 결정되지 않음 -> 계속 왔다갔다
# determinate = 처음부터 끝까지 차는게 계속반복
# progressbar = ttk.Progressbar(root, maximum = 100, mode = "indeterminate")
# progressbar = ttk.Progressbar(root, maximum = 100, mode = "determinate") 
# progressbar.start(10) # 10ms 마다 움직임
# progressbar.pack()


# def btncmd():
#     progressbar.stop() # 작동 중지, 값은 사라짐

# btn = Button(root, text = "stop", command = btncmd)
# btn.pack()

p_var2 = DoubleVar() # 실수 반영
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2) 
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): 
        time.sleep(0.01) # 0.01 초 대기 

        # progress bar 값 설정
        p_var2.set(i)
        # gui update
        progressbar2.update()
        print(p_var2.get())

btn = Button(root, text = "start", command = btncmd2)
btn.pack()

root.mainloop() 