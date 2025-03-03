from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("**********************************MENU**********************************")
    print("***    1. Them sinh vien.                                           ***")
    print("***    2. Cap nhat thong tin sinh vien boi ID.                      ***")
    print("***    3. Xoa sinh vien boi ID.                                      ***")
    print("***    4. Tim kiem sinh vien theo ten.                               ***")
    print("***    5. Sap xep sinh vien theo diem trung binh.                    ***")
    print("***    6. Sap xep sinh vien theo ten.                                ***")
    print("***    7. Hien thi danh sach sinh vien.                              ***")
    print("***    0. Thoat                                                     ***")
    print("************************************************************************")

    try:
        key = int(input("Nhap tuy chon: "))
    except ValueError:
        print("\nVui long nhap so nguyen hop le!")
        continue

    if key == 1:
        print("\n1. Them sinh vien.")
        qlsv.them_sinh_vien()
        print("\nThem sinh vien thanh cong!")

    elif key == 2:
        if qlsv.so_luong_sinh_vien() > 0:
            print("\n2. Cap nhat thong tin sinh vien.")
            try:
                id = int(input("\nNhap ID: "))
                qlsv.cap_nhat_sinh_vien(id)
            except ValueError:
                print("\nID phai la so nguyen!")
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 3:
        if qlsv.so_luong_sinh_vien() > 0:
            print("\n3. Xoa sinh vien.")
            try:
                id = int(input("\nNhap ID: "))
                if qlsv.xoa_sinh_vien_theo_id(id):
                    print("\nSinh vien co ID =", id, "da bi xoa.")
                else:
                    print("\nSinh vien co ID =", id, "khong ton tai.")
            except ValueError:
                print("\nID phai la so nguyen!")
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 4:
        if qlsv.so_luong_sinh_vien() > 0:
            print("\n4. Tim kiem sinh vien theo ten.")
            ten = input("\nNhap ten de tim kiem: ")
            ket_qua_tim_kiem = qlsv.tim_kiem_theo_ten(ten)
            qlsv.hien_thi_danh_sach_sinh_vien(ket_qua_tim_kiem)
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 5:
        if qlsv.so_luong_sinh_vien() > 0:
            print("\n5. Sap xep sinh vien theo diem trung binh.")
            qlsv.sap_xep_theo_diem()
            qlsv.hien_thi_danh_sach_sinh_vien(qlsv.get_list_sinh_vien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 6:
        if qlsv.so_luong_sinh_vien() > 0:
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sap_xep_theo_ten()
            qlsv.hien_thi_danh_sach_sinh_vien(qlsv.get_list_sinh_vien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 7:
        if qlsv.so_luong_sinh_vien() > 0:
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.hien_thi_danh_sach_sinh_vien(qlsv.get_list_sinh_vien())
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 0:
        print("\nBan da chon thoat chuong trinh!")
        break

    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")
