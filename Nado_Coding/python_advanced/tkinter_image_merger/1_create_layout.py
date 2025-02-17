import  tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title = ("Image Merger")

# file frame (add file, delete file)
file_frame = Frame(root)
file_frame.pack(fill = X, padx = 5, pady = 5)

btn_add_file = Button(file_frame, padx = 5, pady = 5, width = 12,  text = "Add File")
btn_add_file.pack(side = LEFT)

btn_delete_file = Button(file_frame, padx = 5, pady = 5, width = 12, text = "Delete File")
btn_delete_file.pack(side = RIGHT)

# list frame
list_frame = Frame(root)
list_frame.pack(fill = BOTH, padx = 5, pady = 5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side = RIGHT, fill = Y)

list_file = Listbox(list_frame, selectmode = EXTENDED, height = 15, yscrollcommand = scrollbar.set)
list_file.pack(side = LEFT, fill = BOTH, expand = True)
scrollbar.config(command = list_file.yview)

# save path
path_frame = LabelFrame(root, text = "save path")
path_frame.pack(fill = X, padx = 5, pady = 5, ipady = 5)

txt_dest_path = Entry(path_frame)
# innerpad height
txt_dest_path.pack(side = LEFT, fill = X, expand = True, padx = 5, pady = 5, ipady = 4)

btn_dest_path = Button(path_frame, text = "search", width = 10)
btn_dest_path.pack(side = RIGHT, padx = 5, pady = 5)

# option frame
frame_option = LabelFrame(root, text = "option")
frame_option.pack(padx = 5, pady = 5, ipady = 5)

# 가로 넓이
# 가로넓이 레이블
lbl_width = Label(frame_option, text = "width", width = 8)
lbl_width.pack(side = LEFT, padx = 5, pady = 5)

# 가로넓이 콤보
opt_width = ["원본 유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state = "readonly", values = opt_width, width = 10 )
cmb_width.current(0)
cmb_width.pack(side = LEFT, padx = 5, pady = 5)

# 간격
# 간격 옵션 레이블
lbl_space = Label(frame_option, text = "space", width = 8)
lbl_space.pack(side = LEFT, padx = 5, pady = 5)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state = "readonly", values = opt_space, width = 10 )
cmb_space.current(0)
cmb_space.pack(side = LEFT, padx = 5, pady = 5)


# 포맷
# 파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text = "file format", width = 8)
lbl_format.pack(side = LEFT, padx = 5, pady = 5)

# 파일 포맷 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state = "readonly", values = opt_format, width = 10 )
cmb_format.current(0)
cmb_format.pack(side = LEFT, padx = 5, pady = 5)

# progress bar
frame_progress = LabelFrame(root, text = "Progress")
frame_progress.pack(fill = X, padx = 5, pady = 5, ipady = 5)

p_bar = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum = 100, variable = p_bar)
progress_bar.pack(fill = X, padx = 5, pady = 5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill = X, padx = 5, pady = 5)

btn_close = Button(frame_run, padx = 5, pady = 5, text = "close", width = 12, command = root.quit)
btn_close.pack(side = RIGHT, padx = 5, pady = 5)

btn_start = Button(frame_run, padx = 5, pady = 5, text = "start", width = 12)
btn_start.pack(side = RIGHT, padx = 5, pady = 5)




root.resizable(False, False) 
root.mainloop()