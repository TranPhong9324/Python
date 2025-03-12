from HinhHoc import HinhHoc

class DanhSachHinhHoc:
    def __init__(self):
        self.danhSach = []

    def themHinh(self, hh):
        if isinstance(hh, HinhHoc):
            self.danhSach.append(hh)

    def xuat(self):
        for hinh in self.danhSach:
            print(f"{type(hinh).__name__}: Diện tích = {hinh.dienTich():.2f}, Chu vi = {hinh.chuVi():.2f}")

    def timHinhCoDienTichLonNhat(self):
        return max(self.danhSach, key=lambda h: h.dienTich(), default=None)

    def timHinhCoDienTichNhoNhat(self):
        return min(self.danhSach, key=lambda h: h.dienTich(), default=None)

    def timHinhTronCoDienTichLonNhat(self):
        hinhTron = [h for h in self.danhSach if isinstance(h, hinhTron)]
        return max(hinhTron, key=lambda h: h.dienTich(), default=None)

    def sapGiamTheoDienTich(self):
        self.danhSach.sort(key=lambda h: h.dienTich(), reverse=True)

    def demSoLuongHinh(self, loaiHinh):
        return sum(1 for h in self.danhSach if isinstance(h, loaiHinh))

    def tinhTongDienTich(self):
        return sum(h.dienTich() for h in self.danhSach)

    def timHinhCoDienTichLonNhatTheoLoai(self, loaiHinh):
        hinhLoai = [h for h in self.danhSach if isinstance(h, loaiHinh)]
        return max(hinhLoai, key=lambda h: h.dienTich(), default=None)

    def timViTriCuaHinh(self, h):
        for idx, hinh in enumerate(self.danhSach):
            if hinh == h:
                return idx
        return -1

    def xoaTaiViTri(self, viTri):
        if 0 <= viTri < len(self.danhSach):
            del self.danhSach[viTri]
            return True
        return False

    def timHinhTheoDTich(self, dt):
        return [h for h in self.danhSach if abs(h.dienTich() - dt) < 1e-9]

    def xoaHinh(self, hh):
        try:
            self.danhSach.remove(hh)
            return True
        except ValueError:
            return False

    def xoaHinhTheoLoai(self, loaiHinh):
        self.danhSach = [h for h in self.danhSach if not isinstance(h, loaiHinh)]

    def xuatHinhTheoChieuTangGiam(self, loaiHinh, tang=True):
        hinhLoai = [h for h in self.danhSach if isinstance(h, loaiHinh)]
        hinhLoai.sort(key=lambda h: h.dienTich(), reverse=not tang)
        for hinh in hinhLoai:
            print(f"{type(hinh).__name__}: Diện tích = {hinh.dienTich():.2f}, Chu vi = {hinh.chuVi():.2f}")

    def tinhTongDTTheoKieuHinh(self, loaiHinh):
        return sum(h.dienTich() for h in self.danhSach if isinstance(h, loaiHinh))
