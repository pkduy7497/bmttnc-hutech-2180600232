#hàm tính giờ làm
so_gio_lam = float(input("Nhập số giờ làm tiêu chuẩn mỗi tuần: "))
luong_gio = float(input("Nhập số tiền thù lao mỗi giờ tiêu chuẩn: "))
gio_tieu_chuan = 44 # Số giờ làm tiêu chuẩn mỗi tuần
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan) # số giờ làm vượt tiêu chuẩn mỗi tuần
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print(f"so tien thuc linh cua nhan vien: {thuc_linh}")