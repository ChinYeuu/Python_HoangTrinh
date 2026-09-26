"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
print("--- ATM Rút tiền ---")
so_du = float(input("Nhập số dư hiện tại: "))
so_tien_rut = float(input("Nhập số tiền muốn rút: "))

if so_tien_rut > 0:
    if so_tien_rut <= so_du:
        if so_tien_rut % 50_000 == 0:
            so_du -= so_tien_rut
            print(f"Rút tiền thành công! Số dư còn lại: {int(so_du):,} VNĐ")
        else:
            print("Thất bại: Số tiền rút phải là bội số của 50,000 VNĐ.")
    else:
        print("Thất bại: Không đủ số dư.")
else:
    print("Thất bại: Số tiền rút không hợp lệ (phải lớn hơn 0).")



# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
print("\n--- Xếp loại BMI ---")
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))

if chieu_cao > 0 and can_nang > 0:
    bmi = can_nang / (chieu_cao ** 2)
    print(f"Chỉ số BMI của bạn: {bmi:.2f}")
    if bmi < 18.5:
        print("Xếp loại: Thiếu cân. Gợi ý: Bạn nên bổ sung dinh dưỡng để tăng cân hợp lý!")
    elif bmi <= 24.9:
        print("Xếp loại: Bình thường. Tuyệt vời! Bạn có vóc dáng rất cân đối.")
    elif bmi <= 29.9:
        print("Xếp loại: Thừa cân. Cảnh báo nhẹ: Bạn nên kiểm soát chế độ ăn uống và tập luyện.")
    else:
        print("Xếp loại: Béo phì. Khuyến nghị: Bạn nên gặp bác sĩ hoặc chuyên gia dinh dưỡng để được tư vấn.")
else:
    print("Lỗi: Chiều cao và cân nặng phải lớn hơn 0.")


# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
print("\n--- Máy bán vé xem phim ---")
loai_ve = input("Nhập loại vé (thuong/vip): ").strip().lower()
ngay = input("Nhập ngày xem (thuong/cuoi_tuan): ").strip().lower()
tuoi = int(input("Nhập tuổi của bạn: "))

# Giá vé cơ bản
if loai_ve == "vip":
    gia_ve = 120_000
else:
    gia_ve = 80_000

# Phụ thu cuối tuần (+30%)
if ngay == "cuoi_tuan":
    gia_ve *= 1.3

# Giảm giá theo độ tuổi
if tuoi < 12 or tuoi >= 65:
    gia_ve *= 0.5
elif 18 <= tuoi <= 25:
    gia_ve *= 0.8

print(f"Giá vé cuối cùng: {int(gia_ve):,} VNĐ")

