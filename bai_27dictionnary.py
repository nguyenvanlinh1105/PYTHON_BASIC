"""
Dictionary: Từ điển được sử dụng để lưu trữ các giá trị dữ liệu trong các cặp key:value

- Từ điển là một tập hợp được sắp xếp theo thứ tự *, có thể thay đổi và không cho phép trùng lặp 
- Kể từ phiên bản Python 3.7, các từ điển được sắp xếp theo tứ tự 
- Từ điển được viết bằng dấu ngoặc nhọn có khóa và giá trị 
- Từ điển có thể thay đổi, nghĩa là chúng có thể thay đổi, thêm hoặc bớt các mục sau khi từ điển đã được tạo 
"""

Sinhvien={
    "HoVaTen":"Nguyễn Văn Linh",
    "maLop":"22T2"
}
Sinhvien1={
    "HoVaTen":"Nguyễn Văn Hào",
    "maLop":"22T3"
}
list =[Sinhvien,Sinhvien1]
tuple =(Sinhvien)
print(Sinhvien)
# lấy dữ liệu
print(Sinhvien["HoVaTen"])
# cách 2: 
print(Sinhvien.get("maLop"))

# thay đổi giá trị 
Sinhvien["maLop"]="DH02"
Sinhvien.update({"linh nguyen":"deptry"}) # có thể thêm mới hoặc thêm giá trị 

# thêm mục mới 
Sinhvien["namHoc"]=2024
Sinhvien["noiSinh"]="Giolinh"

# xóa đi các mục 
Sinhvien.pop("noiSinh")  # loại bỏ mục có tên khóa được chỉ định

# popitem() xóa mục được chèn cuối cùng 
Sinhvien.popitem()

# xóa luôn 
del Sinhvien["HoVaTen"]

# làm trống dictionnary
Sinhvien.clear()

# duyệt các giá trị 
for x in Sinhvien1.values():
    print(x)
# duyet key
for x in Sinhvien1.keys():
    print(x)
# duyệt các cặp khóa -item
for x, y in Sinhvien1.items():
    print(x,y)


print(list)
print(tuple)



