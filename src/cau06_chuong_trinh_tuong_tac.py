ma_phien = input("Nhap ma phien:")
ma_may = input("Nhap ma may:")
cong_suat_w= float(input("Nhap cong suat W:"))
so_phut = int(input("Nhap so phut:"))
don_gia_kwh = float(input("Nhap don gia dien/kWh:"))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print(f"Ma phien: {ma_phien}")
print(f"Ma may: {ma_may}")
print(f"Đien nang tieu thu: {dien_nang_kwh} kWh")
print(f"Chi phi dien: {chi_phi} VND")