# HinhTron.py
from math import pi
from HinhHoc import HinhHoc

class HinhTron(HinhHoc):
    def __init__(self, banKinh):
        self.banKinh = banKinh

    def dienTich(self):
        return pi * self.banKinh ** 2

    def chuVi(self):
        return 2 * pi * self.banKinh