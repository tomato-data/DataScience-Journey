from tkinter import *

root = Tk()
root.title = ("GUI")
root.geometry("640x480")

# selectmode
# single 은 여러개 선택 불가, 하나만/ extended 는 여러개 선택 가능
# height 0은 리스트 전체 보이기. ex) 3을 넣으면 바나나까지보이고 키보드로 내려야 함 
# 왜인지 extended 적용이 안됨
listbox = Listbox(root, selectmode = EXTENDED, height = 0)
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
# END를 쓰면 그냥 끝에 붙임 => append
listbox.insert(END, "watermelon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    # listbox.delete(END) # 맨 뒤 삭제/ 0 을 넣으면 맨 첫번째 삭제
    # 갯수 확인
    # print("in the list:", listbox.size(), "items")

    # 항목 확인 (start idx, end idx)
    # print("1~3:", listbox.get(0, 2))

    # 선택 항목 확인 (returns idx)
    print("selected item:", listbox.curselection())


btn = Button(root, text = "click", command = btncmd)
btn.pack()

root.mainloop()