from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from sinh_vien import SinhVien
import datetime
class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []

    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSVTheoMS(self, ms: str):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == ms:
                return i
        else:
            return -1

    def timSvTheoLoai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]

    # tìm sinh viên có điểm rèn luyện từ 80 trở lên
    def timSinhVienDiemRenLuyen(self, diemRL_min: int = 80):
        return [
            sv for sv in self.dssv
            if isinstance(sv, SinhVienChinhQuy) and sv.diemRL >= diemRL_min
        ]

    # 2. Tìm sinh viên có trình độ cao đẳng sinh trước 15/8/1999
    def timSinhVienCaoDangTruocNgay(self, ngay: str = "15/8/1999"):
        ngay_chuan = datetime.strptime(ngay, "%d/%m/%Y")
        return [
            sv for sv in self.dssv
            if isinstance(sv, SinhVienPhiCQ)
            and sv.trinhDo == "cao đẳng"
            and sv._ngaySinh < ngay_chuan
        ]