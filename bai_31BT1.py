class Ngay:
    def __init__(self, ngay, thang, nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def ngayTrongThang(self, thang, nam):
        if thang in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif thang in [4, 6, 9, 11]:
            return 30
        elif thang == 2:
            if (nam % 400 == 0) or (nam % 100 != 0 and nam % 4 == 0):
                return 29
            else:
                return 28
    def ngayTrongNam(self):
        tongNgay = 0
        for x in range(1, 12+1):
            tongNgay += self.ngayTrongThang(x,self.nam)
        return tongNgay
# Sử dụng lớp Ngay
ngay_obj = Ngay(1, 2, 2024)  # Thêm giá trị ngày, tháng, năm tùy ý
so_ngay = ngay_obj.ngayTrongThang(3,2024)
print(f"Số ngày trong tháng là: {so_ngay}")
so_ngay = ngay_obj.ngayTrongNam()
print("Tổng số ngày trong năm là : " +str(so_ngay))
