import random

Set = set()

while True:
    print("-----MENU------")
    print("1 - Thêm một số điện thoại vào thùng phiếu dự thưởng ")
    print("2 - Xóa một số điện thoại từ thùng phiếu dự thưởng")
    print("3 - Quay số ngẫu nhiên lấy ra một số điện thoại trúng thưởng ")
    print("Thùng phiếu hiện tại:")
    print(Set)
    print("4 - Kết thúc chương trình")

    luachon = int(input("Lựa chọn: "))

    if luachon == 1:
        n = int(input("Nhập vào mã số dự thưởng: "))
        Set.add(n)
    elif luachon == 2:
        m = int(input("Nhập vào mã số dự thưởng cần xóa: "))
        Set.discard(m)
    elif luachon == 3:
        if len(Set) > 0:
            index = random.randint(0,len(Set))
            print("Vị trí trúng thưởng là: "+str(index))
            for i in range(len(Set)) :
                if(i==index):
                    print("Chúc mừng mã số "+ Set[i]+" đã trúng thưởng")
                    Set.discard(Set[i])
        else:
            print("Không có mã số dự thưởng để quay.")
    else:
        break
