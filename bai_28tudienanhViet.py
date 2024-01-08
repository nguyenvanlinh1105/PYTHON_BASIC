Dictionary={

}

while(True):
    print("-----MENU-----")
    print("1. Thêm từ mới")
    print("2. Xóa một từ vừng ")
    print("3. Tra cứu một từ vựng")
    print("4. Cập nhật ý nghĩa cho một từ vựng")
    print("5. Cho phép người dùng xóa toàn bộ từ vựng")
    print("6. Cho phép người dùng in ra toàn bộ từ vựng")
    print("7. Cho phép người dùng in ra toàn bộ từ điển theo cấu trúc TỪ VỰNG: Ý NGHĨA")
    print("8. Kết thúc chương trình")

    luaChon = int(input("Nhập lựa chọn của bạn: "))
    if luaChon ==1:
        tu= input("Nhập từ mới:")
        nghia=input("Nhập ý nghĩa của từ mới: ")

        Dictionary.update({tu:nghia})
    elif luaChon==2:
        xoa = input("Nhập từ cần xóa: ")
        if xoa in Dictionary.keys():
            Dictionary.pop(xoa)
            print("Đã xóa "+xoa+" thành công!")
        else:
            print("Không tồn tại từ "+xoa+" trong từ điển")
    elif luaChon==3:
        traCuu = input("Nhập từ cần tra cứu: ")
        if traCuu in Dictionary.keys():
            ynghia=Dictionary.get(traCuu)
            print("Nghĩa của từ bạn vừa tra là: "+ynghia)
        else:
            print("Không tồn tại từ "+traCuu+" trong từ điển, xin đợi cập nhật lần sau")
    elif luaChon==4:
        capnhatKey = input("Bạn muốn cập nhật cho từ vừng nào: ")
        ynghiaMoi= input("Nghĩa của từ bạn muốn cập nhật là gì: ")
        if capnhatKey in Dictionary.keys():
             Dictionary.update({capnhatKey:ynghiaMoi})
             print("Đã cập nhật thành công !")
        else:
            print("Không tồn tại từ bạn muốn cập nhật")
    elif luaChon==5:
        xacnhan= input("Bạn có chắc chắn muốn xóa hết từ vựng trong từ điển hay không, nhấn phím 1 để xác nhận:")
        xacnhan = int(xacnhan)
        if xacnhan==1:
            Dictionary.clear()
            print("Đã xóa toàn bộ từ vừng trong từ điển")
        else:
            print("Bạn đã xác nhận không xóa toàn bộ từ vựng trong từ điển")
    elif luaChon==6:
        for x in Dictionary.keys():
            print(x)
    elif luaChon==7:
        for key, value in Dictionary.items():
            print(key+":"+value)
    else:
        break