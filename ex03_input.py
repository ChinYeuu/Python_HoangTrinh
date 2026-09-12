"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
name = "Trinh"
print(f"Xin chao {name}!")


# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
tuoi =int(input("Nhap nam sinh: "))
namsinh = 2026 - tuoi
print("So tuoi cua toi la:", namsinh)

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
so_1 =int(input("Nhap so thu nhat: "))
so_2 =int(input("Nhap so thu hai: "))
print("Tong hai so la:", so_1 + so_2)

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
ten = (input("Nhap ten: "))
con_vat = (input("Nhap ten con vat ban thich: "))
so = int(input("So yeu thich la: "))
print("Chuyen hai huoc haha la", ten, con_vat, so)
