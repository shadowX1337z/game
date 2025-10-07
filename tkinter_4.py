import tkinter,time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x400")
root.title("Đăng kí")
root.config(bg = "#00ffd5")
root.resizable(width=False,height=False)

# === HIỆU ỨNG NÚT ===
def trong_nut(event):
    dang_ky_button.config(bg="#32d424")
def ra_ngoai_nut(event):
        dang_ky_button.config(bg="#00ff22")
# === HÀM GHI LOG ===
def click_vao_nhap_password(event):
     time_luu_info = time.localtime()
     print(f"[LOG]>[{time_luu_info.tm_hour}:{time_luu_info.tm_min}:{time_luu_info.tm_sec}] >Người dùng click vào ô nhập liệu mật khẩu")
def nhap_vao_nhap_password(event):
     time_luu_info = time.localtime()
     print(f"[LOG]>[{time_luu_info.tm_hour}:{time_luu_info.tm_min}:{time_luu_info.tm_sec}] >Người dùng nhập vào ô nhập liệu password")
def nhap_vao_nhap_name(event):
     time_luu_info = time.localtime()
     print(f"[LOG]>[{time_luu_info.tm_hour}:{time_luu_info.tm_min}:{time_luu_info.tm_sec}] >Người dùng nhập vào ô nhập liệu tên")
def click_vao_nhap_name(event):
     time_luu_info = time.localtime()
     print(f"[LOG]>[{time_luu_info.tm_hour}:{time_luu_info.tm_min}:{time_luu_info.tm_sec}] >Người dùng click vào ô nhập liệu tên")

# === CÁC THÀNH PHẦN GIAO DIỆN ===
dang_ki_head = Label(root,text="ĐĂNG KÍ",fg="#2200ff",bg="#00ffd5",font=("Arial",20))
dang_ky_ten_head = Label(root,text="Nhập tên tại đây",fg="#00407d")
dang_ky_password_head = Label(root,text="Nhập mật khẩu tại đây",fg="#00407d")
dang_ky_ten = Entry(root,width=35,font=("Arial",14))
dang_ky_password = Entry(root,width=35,font=("Arial",14),show = "*")

# === DANH SÁCH NGƯỜI DÙNG ===
luu_list_user = {}

def luu_info():
    name = dang_ky_ten.get()
    password = dang_ky_password.get()
    if name == "" or password == "":
         messagebox.showinfo("LỖI ĐĂNG KÍ","THIẾU THÔNG TIN ĐĂNG NHẬP")
         return False
    else:
        luu_list_user[name] = password
        return True

def bam_nut_dang_ki():
    if luu_info():  # nếu lưu thành công
        xu_li_nut_dang_ki()
        messagebox.showinfo("THÔNG BÁO", "Đăng kí thành công!")

#====hàm xử lí click vào nút đăng kí ===
def xu_li_nut_dang_ki():
    name = dang_ky_ten.get()
    password = dang_ky_password.get()
    time_luu_info = time.localtime()
    print(f"[LOG]>[{time_luu_info.tm_hour}:{time_luu_info.tm_min}:{time_luu_info.tm_sec}] |NAME_USER|>{name}")
    print(f"[LOG]>[{time_luu_info.tm_hour}:{time_luu_info.tm_min}:{time_luu_info.tm_sec}] |PASSWORD|>{password}")

#===tạo nút đăng kí===
dang_ky_button = Button(root,text="ĐĂNG KÍ",fg="#b300ff",bg="#00ff22",font=("Arial",15),command=bam_nut_dang_ki)


# === ĐẶT VỊ TRÍ ===
dang_ki_head.place(x=180,y=34)
dang_ky_ten_head.place(x=58,y=80)
dang_ky_ten.place(x=57,y=100)
dang_ky_password_head.place(x=58,y=180)
dang_ky_password.place(x=57,y=200)
dang_ky_button.place(x=190,y=270)

# === GẮN SỰ KIỆN ===
dang_ky_button.bind("<Enter>",trong_nut)
dang_ky_button.bind("<Leave>",ra_ngoai_nut)
dang_ky_ten.bind("<FocusIn>",click_vao_nhap_name)
dang_ky_ten.bind("<Key>",nhap_vao_nhap_name)
dang_ky_password.bind("<FocusIn>",click_vao_nhap_password)
dang_ky_password.bind("<Key>",nhap_vao_nhap_password)

root.mainloop()