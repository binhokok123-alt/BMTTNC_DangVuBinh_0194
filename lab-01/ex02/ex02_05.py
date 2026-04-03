so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập lương mỗi giờ làm tiêu chuẩn: "))
gio_tieu_chuan = 44
giơ_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + giơ_vuot_chuan * luong_gio * 1.5
print(f"Số tiền thực lĩnh hàng tuần là: {thuc_linh}")