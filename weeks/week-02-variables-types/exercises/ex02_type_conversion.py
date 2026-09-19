"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
print("\n Cau 1:")
so_text = "42"
so_int = int(so_text)
so_int += 8
print("Ket qua la:", so_int)

# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
print("\n Cau 2:")
pi = 3.14159
print("Ket qua khi chuyen sang int se duoc la:",int(pi))

# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
print("\n Cau 3:")
print("bool(0):",bool(0))
print("bool(1):",bool(1))
print("bool(""):",bool(""))
print("bool('hello'):",bool("hello"))
print("bool([])",bool([]))
print("bool([1,2]): ",bool([1,2]))


# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
print("\n Cau 4:")
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"Chỉ số BMI la: {bmi:.1f}")


# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
print("\n Cau 5:")
tong_giay = int(input("Nhập số giây: "))
gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60
print(f"{tong_giay} giây → {gio} giờ {phut} phút {giay} giây")
