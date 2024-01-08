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
        if m in Set:
            Set.remove(m)
        else:
            print("Mã số dự thưởng không tồn tại trong thùng phiếu.")
    elif luachon == 3:
        if len(Set) > 0:
            index = random.randint(0, len(Set) - 1)
            winner = list(Set)[index]
            print("Chúc mừng mã số " + str(winner) + " đã trúng thưởng")
            Set.discard(winner)
        else:
            print("Không có mã số dự thưởng để quay.")
    else:
        break
