from tkinter import *

root = Tk()
root.title = ("GUI")

btn1 = Button(root, text = "button1")
btn1.pack()

# pad = 버튼 크기를 키움/ 버튼222라는 글자를 기준으로 공간을 확보
btn2 = Button(root, padx = 5, pady = 10, text = "button2222222")
btn2.pack()

btn3 = Button(root, padx = 10, pady = 5, text = "button3")
btn3.pack()

# 버튼 크기자체를 설정/ 텍스트 길이가 길어져도 텍스트가 잘릴지언정 버튼크기는 고정
btn4 = Button(root, width = 10, height = 3, text = "button4")
btn4.pack()

# mac이라 그런지 bg가 그냥 하얀색
btn5 = Button(root, fg = "red", bg = "yellow", text = "button5")
btn5.pack()

# 
photo = PhotoImage(file = "/Users/lofichill/Desktop/python/study/\
nado coding/applied python/gui_basic/check.png")
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print("button has been clicked")

btn7 = Button(root, text = "working", command = btncmd)
btn7.pack()


root.mainloop()