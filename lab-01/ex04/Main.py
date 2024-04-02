#Tạo Menu
from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\n CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("*************************MENU*************************")
    print("** 1. Thêm Sinh Viên.                               **")
    print("** 2. Cập nhật thông tin SV bởi ID.                 **")
    print("** 3. Xoá SV bởi ID.                                **")
    print("** 4. Tìm kiếm SV theo tên.                         **")
    print("** 5. Sắp xếp SV theo điểm TB.                      **")
    print("** 6. Sắp xếp SV theo Chuyên Ngành.                 **")
    print("** 7. Hiển thị danh sách sinh viên.                 **")
    print("** 0. Thoát.                                        **")
    print("******************************************************")
    
    key = int(input("Nhập số tuỳ chọn (0 đến 7): "))
    if (key == 1):
        print("\nl. Thêm sinh viên.")
        qlsv.nhapSinhVien ()
        print ("\nThêm sinh viên thành công!")
    elif (key == 2):
        if (qlsv.soluongSinhVien() > 0):
            print("\n2. Cập nhật thông tin SV. ")
            print("\nNhập ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print ("\nDanh sách sinh viên trống !!!")
    elif (key == 3):
        if (qlsv.soluongSinhVien() > 0):
            print("\n3. Xoá sinh viên.")
            print("\nNhập ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh viên có ID = ", ID, " đã bị xoá.")
            else:
                print("\nSinh viên có ID = ", ID ," không tồn tại.")
        else:
            print ("\nDanh sách sinh viên trống !!!")
    elif (key == 4):
        if(qlsv.soluongSinhVien () > 0):
            print("\n4. Tìm kiếm sinh viên theo tên. ")
            print("\nNhập tên để tìm kiếm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print ("\nDanh sách sinh viên trống!!!")
    elif (key == 5):
        if (qlsv.soluongSinhVien() > 0):
            print("\n5. Sắp xếp sinh viên theo điểm trung bình (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống!!!")
    elif (key == 6):
        if (qlsv.soluongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên theo tên.")
            qlsv.sortByName()
            qlsv.showsinhvien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống!!!")
    elif (key == 7):
        if (qlsv.soluongSinhVien() > 0):
            print("\a7. Hiển thị danh sách sinh viên.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print ("\nDanh sách sinh viên trống!!!")
    elif (key == 0):
        print("\nBạn đã chọn thoát chương trình!!!")
        break
    else:
        print("\nKhông có chức năng này !!!")
        print("\nHãy chọn những chức năng trong Menu. Cảm ơn !!!")

