ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhap so phut: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")

# Loi 1 (SyntaxError - Dong 6): Lenh print cuoi cung thieu dau dong ngoac tron ')'.
# Loi 2 (TypeError - Dong 2 & 4): Bien cong_suat_w chua duoc chuyen sang float dan den phep nhan chuoi va loi khi chia cho 60.
# Loi 3 (NameError - Dong 6): Goi sai ten bien 'dien_nang' trong f-string (ten dung da khai bao la 'dien_nang_kwh').