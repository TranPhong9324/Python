# main.py
from HinhTron import HinhTron
from HinhChuNhat import HinhChuNhat
from HinhVuong import HinhVuong
from DanhSachHinhHoc import DanhSachHinhHoc

if __name__ == "__main__":
    dsHinh = DanhSachHinhHoc()

    hinhTron = HinhTron(5)
    hinhChuNhat = HinhChuNhat(4, 6)
    hinhVuong = HinhVuong(3)

    dsHinh.themHinh(hinhTron)
    dsHinh.themHinh(hinhChuNhat)
    dsHinh.themHinh(hinhVuong)

    print("Danh sách hình:")
    dsHinh.xuat()

    hinhLonNhat = dsHinh.timHinhCoDienTichLonNhat()
    if hinhLonNhat:
        print(f"Hình có diện tích lớn nhất: {type(hinhLonNhat).__name__} với diện tích {hinhLonNhat.dienTich():.2f}")

    hinhNhoNhat = dsHinh.timHinhCoDienTichNhoNhat()
    if hinhNhoNhat:
        print(f"Hình có diện tích nhỏ nhất: {type(hinhNhoNhat).__name__} với diện tích {hinhNhoNhat.dienTich():.2f}")

    tongDienTich = dsHinh.tinhTongDienTich()
    print(f"Tổng diện tích tất cả hình: {tongDienTich:.2f}")
