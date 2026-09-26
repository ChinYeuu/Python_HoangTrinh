"""
Bài tập 01: if/elif/else cơ bản 🔀
====================================
Mục tiêu: Viết câu lệnh điều kiện đúng cú pháp
"""

# TODO 1: Nhập tuổi, in ra nhóm tuổi
# < 13: "Thiếu nhi"
# 13-17: "Thiếu niên"
# 18-64: "Người lớn"
# >= 65: "Người cao tuổi"
print ("Cau 1\n")
tuoi = int(input("Nhap tuoi: "))

if tuoi < 13 :
    print ("Thieu nhi")
elif tuoi <= 17 :
    print ("Thieu nien")
elif tuoi <= 64 :
    print (" Nguoi lon")
else :
    print ("Nguoi cao tuoi")
    

# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu
print ("Cau 2\n")
diem = float(input("Nhap diem: "))

if diem >= 9 :
    print("Xuat sac")
elif diem >= 8 :
    print("Gioi")
elif diem >= 6.5 :
    print("Kha")
elif diem >= 5 :
    print ("Trung binh")
else :
    print ("Yeu")

# TODO 3: Nhập năm, kiểm tra năm nhuận
# Năm nhuận: chia hết cho 4, NHƯNG không chia hết cho 100,
# TRỪ KHI chia hết cho 400
# 2000 → nhuận, 1900 → không, 2024 → nhuận
print ("Cau 3\n")

nam = int(input("Nhap nam: "))
if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0 :
    print ("Nam nhuan")
else :
    print ("Nam khong nhuan")


# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
print ("Cau 4\n")

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
if a > b and a > c :
    lon_nhat = a
elif b > a and b > c :
    lon_nhat = b
else :
    lon_nhat = c
print("So lon nhat la:", lon_nhat)
