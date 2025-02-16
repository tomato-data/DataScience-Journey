from tkinter import *

root = Tk()
root.title = ("GUI")
root.geometry("640x480") # 가로 x 세로 크기
# root.geometry("640x480+300+100") # x축 위치 + y축 위치 
root.resizable(False, False) # x, y 값 변경 불가 = 창 크기 변경 불가 


# 창이 닫히지 않게
root.mainloop()