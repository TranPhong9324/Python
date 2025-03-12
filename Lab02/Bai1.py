from datetime import datetime

class SinhVien:
    # biến của lớp, chung cho tất cả các đối tượng thuộc lớp
    truong = "Đại học Đà Lạt"
    
    # Hàm khởi tạo, hàm tạo lập: khởi gán các thuộc tính của đối tượng
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self._maSo = maSo # thuộc tính private
        self._hoTen = hoTen # thuộc tính private
        self._ngaySinh = ngaySinh # thuộc tính private
    
    
    # Cho phép truy xuất tới thuộc tính từ bên ngoài thông qua trường maSo
    @property
    def maSo(self):
        return self._maSo
    
    # Cho phép thay đổi giá trị thuộc tính maSo
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self._maSo = maso
            
    # Phương thức tĩnh: các phương thức không truy xuất gì đến thuộc tính, hành vi của lớp
    # Những phương thức này không cần truyền tham số mặc định self
    # Đấy không phải là một hành vi (phương thức) của một đối tượng thuộc lớp
    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7
    
    # Phương thức của lớp, chỉ truy xuất tới các biến thành viên của lớp
    # không truy xuất được các thuộc tính riêng của đổi tượng
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi
        
    
    # Tương tự ghi đè phương thức toString()
    def __str__(self) -> str:
        return f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}"
    
    # Hành vi của đối tượng sinh viên
    def xuat(self):
        print(f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}")
        
class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []
    
    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)
    
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    
    # Tìm sinh viên theo mssv, nếu có trả về sinh viên
    def timSVTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.mssv == mssv]
    
    # Tìm sinh viên theo mssv, nếu có trả về vị trí của sinh viên trong danh sách
    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1
    
    #xóa sinh viên có mã số mssv, thông báo xóa được hay không
    def xoaSVTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    
    # Tìm sinh viên tên "Nam"
    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen == "Nam"]
    
    # Tìm những sinh viên sinh trước 15/6/2000
    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh]

sv1 = SinhVien(2113018, "Nguyễn Phan Thanh Sang", datetime.strptime("23/08/2003", "%d/%m/%Y"))
sv2 = SinhVien(2115230, "Lê Trần gia My", datetime.strptime("18/09/2002", "%d/%m/%Y"))
sv3 = SinhVien(2115892, "Nguyễn Linh Việt", datetime.strptime("15/09/1999", "%d/%m/%Y"))
sv4 = SinhVien(2114569, "Hoàng Thành Nam", datetime.strptime("13/02/2002", "%d/%m/%Y"))
sv5 = SinhVien(2111111, "Hoàng Trần Phương Nam", datetime.strptime("26/09/2003", "%d/%m/%Y"))
sv6 = SinhVien(2119632, "Huỳnh Văn Kiên", datetime.strptime("19/08/2002", "%d/%m/%Y"))
# sv.xuat()
ds = DanhSachSV()
ds.themSinhVien(sv1)
ds.themSinhVien(sv2)
ds.themSinhVien(sv3)
ds.themSinhVien(sv4)
ds.themSinhVien(sv5)
ds.themSinhVien(sv6)
ds.xuat()