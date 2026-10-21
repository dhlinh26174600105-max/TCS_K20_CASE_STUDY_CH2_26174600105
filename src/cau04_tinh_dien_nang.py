cong_suat_w = 250
so_phut = 90 
don_gia_kwh = 3000
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print(f"Dien nang tieu thu: {dien_nang_kwh}, type: {type(dien_nang_kwh)}")
print(f"Chi phi dien: {chi_phi}, type: {type(chi_phi)}")
# du doan ket qua: dien_nang_kwh = 0.376, chi_phi = 1125.0

cong_suat_w = 250
so_phut = 60
don_gia_kwh = 3000
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print(f"Dien nang tieu thu: {dien_nang_kwh}, type: {type(dien_nang_kwh)}")
print(f"Chi phi dien: {chi_phi}, type: {type(chi_phi)}")
# du doan ket qua: dien_nang_kwh = 0.25, chi_phi = 750.0

