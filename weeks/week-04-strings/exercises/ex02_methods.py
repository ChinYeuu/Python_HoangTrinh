"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
email_clean = email.strip().lower()
print(f'"{email_clean}"')


# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
print("a) Title Case:", sentence.title())
print("b) Số lần xuất hiện của chữ 'o':", sentence.count("o"))
print("c) Thay 'python':", sentence.replace("python", "PYTHON"))


# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
ho_ten = input("Nhập họ tên đầy đủ: ")
parts = ho_ten.strip().split()
if parts:
    print(f'Họ: "{parts[0]}", Tên: "{parts[-1]}"')


# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
file_name = input("Nhập tên file: ")
is_supported = file_name.strip().endswith((".py", ".txt", ".csv"))
print(f"File hợp lệ: {is_supported}")


# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
plain_text = input("Nhập chuỗi cần mã hóa Caesar: ")
shift = int(input("Nhập số bước dịch (shift): "))
cipher_text = ""
for char in plain_text:
    if char.isalpha():
        base = ord("A") if char.isupper() else ord("a")
        cipher_text += chr((ord(char) - base + shift) % 26 + base)
    else:
        cipher_text += char
print("Kết quả mã hóa:", cipher_text)

