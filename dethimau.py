import math

class TuLanh:
    def __init__(self, nhanhieu="Elextrolux", maso="UNKNOWN", nuocsx="Việt Nam", tkdien=True, dungtich=256, gia=7000000):
        self._nhanhieu = nhanhieu
        self._maso = maso
        self._nuocsx = nuocsx
        self._tkdien = tkdien
        self._dungtich = dungtich
        self._gia = gia

    def makeCopy(self, tl):
        if not isinstance(tl, TuLanh):
            raise ValueError("Đối tượng phải là một TuLanh")
        self._nhanhieu = tl._nhanhieu
        self._maso = tl._maso
        self._nuocsx = tl._nuocsx
        self._tkdien = tl._tkdien
        self._dungtich = tl._dungtich
        self._gia = tl._gia

    def nhapThongTin(self):
        self._nhanhieu = input("Nhập nhãn hiệu: ").strip()
        self._maso = input("Nhập mã số: ").strip()
        self._nuocsx = input("Nhập nước sản xuất: ").strip()
        tkdien_input = input("Nhập tiết kiệm điện (true/false): ").strip().lower()
        if tkdien_input not in ("true", "false"):
            raise ValueError("Tiết kiệm điện phải là TRUE hoặc FALSE")
        self._tkdien = (tkdien_input == "true")
        try:
            self._dungtich = int(input("Nhập dung tích (lít): ").strip())
            self._gia = int(input("Nhập giá (VNĐ): ").strip())
        except ValueError:
            raise ValueError("Dung tích và giá phải là số nguyên")

    def hienThi(self):
        print(f"Nhãn hiệu    : {self._nhanhieu}")
        print(f"Mã số       : {self._maso}")
        print(f"Nước SX     : {self._nuocsx}")
        print(f"T/K điện    : {'Có' if self._tkdien else 'Không'}")
        print(f"Dung tích   : {self._dungtich} L")
        print(f"Giá         : {self._gia} VNĐ")

    def layNhanHieu(self):
        return self._nhanhieu

    def layGia(self):
        return self._gia

    def soNguoiSD(self):
        return math.floor(self._dungtich / 100)

    def cungNhanHieu(self, tl):
        if not isinstance(tl, TuLanh):
            raise ValueError("Đối tượng phải là một TuLanh")
        return self._nhanhieu.lower() == tl._nhanhieu.lower()

    def nhHon(self, tl):
        if not isinstance(tl, TuLanh):
            raise ValueError("Đối tượng phải là một TuLanh")
        return self._dungtich < tl._dungtich

if __name__ == "__main__":
    print("Nhập thông tin cho tủ lạnh")
    tl = TuLanh()
    tl.nhapThongTin()
    print("\nThông tin tủ lạnh vừa nhập:")
    tl.hienThi()
    print(f"\nSố người sử dụng phù hợp: {tl.soNguoiSD()}")