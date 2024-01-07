"""
Tuple : là một chuỗi các phần tử có thử tự như một list. Sự khác biệt duy nhất là bộ giá trị là các hằng số 
- Đặc biệt của tuple là khi tạo ra thì giá trị của nó không thể sửa đổi.
- tuple được sử dụng để bảo vệ dữ liệu và thường nhanh hơn danh sách vì chúng không thể thay đổi động 
- Được định nghĩa trong dấu ngoặc đơn(), các mục được phân tách bằng dấu phẩy.
- giá trị của tuple có thể bị trùng lặp 


"""

TraiCay=('Na','Lựu','Hồng','Cam','Quýt')
so=(1,2,3,4,5,6)
print(TraiCay)
print(so)

# Các thao tác với Tuple
# lấy phần tử 
print(so[0])
print(so[1:4])
# Cộng 2 tuple 
y = (1,2, 3, 4, 7,9)
z =('a','g', 'b')
t= y+z
print(t)
# phép nhân 
k = y*2
print(k)


