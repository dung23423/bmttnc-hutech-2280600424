from SinhVien import SinhVien

class QuanLySinhVien:
    ds = []

    def so_luong_sinh_vien(self):
        return len(self.ds)

    def xet_hoc_luc(self, dtb):
        if dtb >= 8:
            return "Gioi"
        elif dtb >= 6.5:
            return "Kha"
        elif dtb >= 5:
            return "Trung Binh"
        else:
            return "Yeu"

    def tim_kiem_theo_id(self, id):
        for sv in self.ds:
            if sv._id == id:
                return sv
        return None

    def tim_kiem_theo_ten(self, ten):
        dssv = []
        for sv in self.ds:
            if ten.upper() in sv._ten.upper():
                dssv.append(sv)
        return dssv

    def tao_id(self):
        id = 1
        if self.so_luong_sinh_vien() > 0:
            max_id = self.ds[0]._id
            for sv in self.ds:
                if max_id < sv._id:
                    max_id = sv._id
            id = max_id + 1
        return id

    def them_sinh_vien(self):
        id = self.tao_id()
        ten = input("Nhap ten sinh vien: ")
        gioi_tinh = input("Nhap gioi tinh sinh vien: ")
        chuyen_nganh = input("Nhap chuyen nganh sinh vien: ")
        dtb = float(input("Nhap diem trung binh: "))

        sv = SinhVien(id, ten, gioi_tinh, chuyen_nganh, dtb)
        sv._hoc_luc = self.xet_hoc_luc(dtb)
        self.ds.append(sv)

    def cap_nhat_sinh_vien(self, id):
        sv = self.tim_kiem_theo_id(id)
        if sv is not None:
            sv._ten = input("Nhap ten sinh vien: ")
            sv._gioi_tinh = input("Nhap gioi tinh sinh vien: ")
            sv._chuyen_nganh = input("Nhap chuyen nganh sinh vien: ")
            sv._dtb = float(input("Nhap diem trung binh: "))
            sv._hoc_luc = self.xet_hoc_luc(sv._dtb)
        else:
            print("Khong co sinh vien can cap nhat.")

    def xoa_sinh_vien_theo_id(self, id):
        sv = self.tim_kiem_theo_id(id)
        if sv is not None:
            self.ds.remove(sv)
            return True
        return False

    def sap_xep_theo_diem(self):
        self.ds.sort(key=lambda sv: sv._dtb, reverse=False)

    def sap_xep_theo_ten_chuyen_nganh(self):
        self.ds.sort(key=lambda sv: sv._chuyen_nganh, reverse=False)

    def hien_thi_danh_sach_sinh_vien(self, ds):
        print("{:<8} {:<18} {:<12} {:<15} {:<8} {:<10}".format(
            "ID", "Ten", "Gioi Tinh", "Chuyen Nganh", "DTB", "Hoc Luc"))
        
        if len(ds) > 0:
            for sv in ds:
                print("{:<8} {:<18} {:<12} {:<15} {:<8} {:<10}".format(
                    sv._id, sv._ten, sv._gioi_tinh, sv._chuyen_nganh, sv._dtb, sv._hoc_luc))
            print("\n")

    def get_list_sinh_vien(self):
        return self.ds
