import os
import  tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog # submodule 이기 때문에 별도로 import 해야함
from PIL import Image

root = Tk()
root.title = ("Image Merger")

# add file
def add_file():
    # 복수의 파일을 선택 할 수 있게
    files = filedialog.askopenfilenames(title = "choose image files", \
        filetypes = (("PNG files", "*.png"), ("all files", "*.*")),\
        initialdir = "/Users/lofichill/Desktop") # 최초에 사용자가 지정한 경로를 보여줌
    
    # 선택한 목록을 출력
    for file in files:
        list_file.insert(END, file)


# del file
def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# save path (folder)
def browse_dest_path():
    # folder selection
    selected_folder = filedialog.askdirectory()
    if selected_folder == '': # 취소를 누를 때
        return
    print(selected_folder)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, selected_folder)

# 실제 이미지 합치는 함수
def merge_image():
    try:
        # 가로 넓이
        img_width = cmb_width.get()
        if img_width == "원본 유지":
            img_width = -1 # -1일 때는 원본 기준으로
        else:
            img_width = int(img_width)

        # 간격
        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else:
            img_space = 0

        # format
        img_format = cmb_format.get().lower() # png, jpg, bmp

        ###################

        images = [Image.open(x) for x in list_file.get(0, END)]

        # image size 하나씩 처리
        image_sizes = [] # [(width1, height1) (width2, height2)...]
        if img_width > -1:
            # width 값 변경
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            # 원본 사이즈 적용
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        # 계산식
        # 100 * 60 -> width 를 80으로 줄이면 height 는?
        # width : hieght = after width : after height

        #[(10, 10), (20, 20), (30, 30)]
        widths, heights = zip(*(image_sizes))
        max_width, total_height = max(widths), sum(heights)
        
        # sketchbook
        if img_space > 0: # applying image space option
            total_height += (img_space * (len(images) - 1))

        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))
        y_offset = 0 # y 위치 정보

        for idx, img in enumerate(images):
            # width 가 원본유지가 아닐 때에는 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space) # height 값 + space

            progress = (idx + 1) / len(images) * 100 # %정보 가져오기
            p_var.set(progress)
            progress_bar.update()
        
        # format option
        file_name = "mergedfile." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("notice", "merging done")

    except Exception as err:
        msgbox.showerror("error", err)

# start
def start():
    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("warning", "no image file added to the list")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("warning", "save path not selected")
        return
    
    merge_image()

# file frame (add file, delete file)
file_frame = Frame(root)
file_frame.pack(fill = X, padx = 5, pady = 5)

btn_add_file = Button(file_frame, padx = 5, pady = 5, width = 12,  text = "Add File", command = add_file)
btn_add_file.pack(side = LEFT)

btn_delete_file = Button(file_frame, padx = 5, pady = 5, width = 12, text = "Delete File", command = del_file)
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

btn_dest_path = Button(path_frame, text = "search", width = 10, command = browse_dest_path)
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

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum = 100, variable = p_var)
progress_bar.pack(fill = X, padx = 5, pady = 5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill = X, padx = 5, pady = 5)

btn_close = Button(frame_run, padx = 5, pady = 5, text = "close", width = 12, command = root.quit)
btn_close.pack(side = RIGHT, padx = 5, pady = 5)

btn_start = Button(frame_run, padx = 5, pady = 5, text = "start", width = 12, command = start)
btn_start.pack(side = RIGHT, padx = 5, pady = 5)


root.resizable(False, False) 
root.mainloop()