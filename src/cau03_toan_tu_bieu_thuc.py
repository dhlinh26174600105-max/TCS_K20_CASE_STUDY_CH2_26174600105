tong_phut = 135
cong_suat_w = 250
so_gio_tron_ven = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print(so_gio_tron_ven)
print(so_phut_con_lai)

su_dung_lau = tong_phut > 60
print(su_dung_lau)

du_lieu_hop_le = cong_suat_w > 0 and tong_phut > 0
print(du_lieu_hop_le)
bieu_thuc_1 = 100 + 20 * 3      #Du doan 160 
bieu_thuc_2 = (100 +20) * 3    #Du doan 360
print(bieu_thuc_1)
print(bieu_thuc_2)