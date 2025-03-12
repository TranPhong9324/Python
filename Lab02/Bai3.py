import math

class PhanSo:
    def __init__(self, tu, mau):
        if mau == 0:
            raise ValueError("Mẫu số không thể bằng 0")
        self.tu = tu
        self.mau = mau
        self.rutGon()

    def rutGon(self):
        gcd = math.gcd(self.tu, self.mau)
        self.tu //= gcd
        self.mau //= gcd
        if self.mau < 0:  # Đảm bảo mẫu luôn dương
            self.tu = -self.tu
            self.mau = -self.mau

    def __add__(self, other):
        tu = self.tu * other.mau + other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    def __sub__(self, other):
        tu = self.tu * other.mau - other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    def __mul__(self, other):
        tu = self.tu * other.tu
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    def __truediv__(self, other):
        if other.tu == 0:
            raise ZeroDivisionError("Không thể chia cho phân số 0")
        tu = self.tu * other.mau
        mau = self.mau * other.tu
        return PhanSo(tu, mau)

    def __str__(self):
        return f"{self.tu}/{self.mau}" if self.mau != 1 else f"{self.tu}"

    def __repr__(self):
        return self.__str__()

    def is_positive(self):
        return self.tu * self.mau > 0

    def is_negative(self):
        return self.tu * self.mau < 0


class DanhSachPhanSo:
    def __init__(self):
        self.danh_sach = []

    def them_phan_so(self, phan_so):
        self.danh_sach.append(phan_so)

    def dem_phan_so_am(self):
        return sum(1 for ps in self.danh_sach if ps.is_negative())

    def tim_phan_so_duong_nho_nhat(self):
        phan_so_duong = [ps for ps in self.danh_sach if ps.is_positive()]
        return min(phan_so_duong, key=lambda ps: ps.tu / ps.mau, default=None)

    def tim_vi_tri_cua_phan_so(self, x):
        return [i for i, ps in enumerate(self.danh_sach) if ps.tu == x.tu and ps.mau == x.mau]

    def tong_phan_so_am(self):
        tong = PhanSo(0, 1)
        for ps in self.danh_sach:
            if ps.is_negative():
                tong += ps
        return tong

    def xoa_phan_so(self, x):
        self.danh_sach = [ps for ps in self.danh_sach if ps.tu != x.tu or ps.mau != x.mau]

    def xoa_phan_so_co_tu(self, tu):
        self.danh_sach = [ps for ps in self.danh_sach if ps.tu != tu]

    def sap_xep_tang_giam(self, tang=True, theo_mau=False):
        if theo_mau:
            self.danh_sach.sort(key=lambda ps: (ps.mau, ps.tu) if tang else (-ps.mau, -ps.tu))
        else:
            self.danh_sach.sort(key=lambda ps: (ps.tu / ps.mau) if tang else -(ps.tu / ps.mau))

    def __str__(self):
        return ", ".join(str(ps) for ps in self.danh_sach)


# Kiểm tra chương trình
if __name__ == "__main__":
    ds = DanhSachPhanSo()
    ds.them_phan_so(PhanSo(3, 4))
    ds.them_phan_so(PhanSo(-2, 5))
    ds.them_phan_so(PhanSo(1, 6))
    ds.them_phan_so(PhanSo(2, 3))

    print("Danh sách phân số:", ds)
    print("Số phân số âm:", ds.dem_phan_so_am())
    print("Phân số dương nhỏ nhất:", ds.tim_phan_so_duong_nho_nhat())
    print("Tổng các phân số âm:", ds.tong_phan_so_am())

    x = PhanSo(1, 6)
    print(f"Vị trí của phân số {x}:", ds.tim_vi_tri_cua_phan_so(x))

    ds.xoa_phan_so(x)
    print("Danh sách sau khi xóa phân số", x, ":", ds)

    ds.sap_xep_tang_giam(tang=True)
    print("Danh sách sau khi sắp xếp tăng:", ds)

    ds.sap_xep_tang_giam(tang=False)
    print("Danh sách sau khi sắp xếp giảm:", ds)
