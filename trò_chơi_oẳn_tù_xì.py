import random
diem_may = 0
diem_nguoi = 0
while True:
  A = random.choice(["kéo","búa","bao"])
  B:str = input("nhap keo bua bao: ")
  if A == B:
    print(f"máy chọn: {A}")
    print(f"người chọn: {B}")
    print("hoà")
  elif (A == "búa" and B == "bao") or \
       (A == "kéo" and B == "búa") or \
       (A == "bao" and B == "kéo"):
      print(f"máy chọn: {A}")
      print(f"người chọn: {B}")
      print("bạn thắng")
  elif (A == "bao" and B == "búa") or \
       (A == "búa" and B == "kéo") or \
       (A == "kéo" and B == "bao"):
      print(f"máy chọn: {A}")
      print(f"người chọn: {B}")
      print("bạn thua")
  elif B == "exit":
    break
  else:
    print("lỗi")
    continue
print("🏆 Kết thúc trò chơi 🏆")
if diem_nguoi > diem_may:
  print("bạn thắng")
elif diem_nguoi < diem_may:
  print("bạn thua")
else:
  print("hoà")
print(f"Điểm bạn: {diem_nguoi}, Điểm máy: {diem_may}")

import random
so_lan_sai = 0
A = random.randint(0,100)
while True:
  B:int = input("nhap so doan: ")
  A = int(A)
  B = int(B)
  if B == A :
    print("hoan hô")
    print(f"số đoán là {A}")
    break
  elif B > A:
    print("nhỏ hơn")
    so_lan_sai += 1
  elif B < A:
    print("lớn hơn")
    so_lan_sai += 1
  elif so_lan_sai == 10:
    print("bạn thua")
    Break
  elif B == 3285:
    Break
  else:
    print("lỗi")
    continue
if so_lan_sai == 10:
  print("số lần sai quá 10 lần")
elif B == "exit":
  print("kết thúc chương trình")
elif B == A:
  print(f"số lần sai là {so_lan_sai}")
