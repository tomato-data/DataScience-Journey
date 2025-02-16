import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title = ("GUI")
root.geometry("640x480")

def info():
    msgbox.showinfo("notice", "reservation completed")

def warn():
    msgbox.showwarning("warning", "selected seats are sold out")

def error():
    msgbox.showerror("error", "payment error")

def okcancel():
    msgbox.askokcancel("ok / cancel", "selected seat is children\
         companion seat proceed?")

def retrycancel():
    msgbox.askretrycancel("retry / cancel", "contemporary error. try again?")

def yesno():
    msgbox.askyesno("yes / no", "selected seat is a backward facing seat.\
     continue?")

def yesnocancel():
    response = msgbox.askyesnocancel(Title = None, message = "reservation not saved.\n\
    save and quit?")
    # yes = save and quit
    # no = don't save and quit
    # cancel = stay
    print("response:", response)
    if response == 1:
        print("yes")
    elif response == 0:
        print("no")
    # 취소 값은 None
    else:
        print("cancel")


Button(root, command = info, text = "notice").pack()
Button(root, command = warn, text = "warning").pack()
Button(root, command = error, text = "error").pack()

Button(root, command = okcancel, text = "ok / cancel").pack()
Button(root, command = retrycancel, text = "retry / cancel").pack()
Button(root, command = yesno, text = "yes / no").pack()
Button(root, command = yesnocancel, text = "yes / no / cancel").pack()


root.mainloop() 