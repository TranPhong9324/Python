from HinhHoc import HinhHoc

class HinhChuNhat(HinhHoc):
    def __init__(self, chieuDai, chieuRong):
        self.chieuDai = chieuDai
        self.chieuRong = chieuRong

    def dienTich(self):
        return self.chieuDai * self.chieuRong

    def chuVi(self):
        return 2 * (self.chieuDai + self.chieuRong)
