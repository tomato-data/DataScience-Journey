import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title = ("GUI")
root.geometry("640x480")

values = ["day" + str(i) for i in range(1, 32)]
combobox = ttk.Combobox(root, height = 5, values = values)
combobox.pack()
combobox.set("payday") # 최초목록 제목설정/ 버튼 클릭을 통한 값 설정도 가능

# state = readonly 읽기 전용, 입력 안됨
# height = 보이는 목록 개수
ronly_combobox = ttk.Combobox(root, height = 10, values = values, state = "readonly")
ronly_combobox.current(0) # 0번째 인덱스 값 선택
ronly_combobox.pack()


def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(ronly_combobox.get())


btn = Button(root, text = "select", command = btncmd)
btn.pack()

root.mainloop() 