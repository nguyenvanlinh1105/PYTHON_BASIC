"""
Set là một trong 4 kiểu dữ liệu tích hợp sẵn trong Python dùng để lưu trữ các tập hợp là dữ liệu, 3 kiểu còn lại là list, Tuple và Dictionary, tất cả đều có chất lượng và cách sử dụng khác nhau 
Set là tập hợp không có thứ tự, không thể thay đổi và không được lập chỉ mục. Lưu ý : Các mục set là không thể thay đổi nhưng bạn có thể xóa và thêm các mục mới 
 Sử dụng cặp ngoặc { }// không trung nhau 
"""

Set ={'Gà','Vịt','Heo','Chó'}
print(Set)

for x in Set:
    print(x)

# xóa 
Set.remove("Gà")# không có là sẽ lỗi
Set.discard("Gà")# không có thì không lỗi
print(Set)
# Làm rỗng
Set.clear()
# xóa Set
del Set

# Loại bỏ phần tử cuỗi mảng bằng phương thức pop 
Set.pop()


# Thêm phần tử 
Set.add("325")
print(Set)
#duyệt 
for it in Set:
    print(it)

Syt={"Trâu","Bò"}
Set.update(Syt)
print(Set)


# Thêm list vào set 
list1 =["Tôi","Muốn","Tôi"]
Set.update(list1)
print(Set)