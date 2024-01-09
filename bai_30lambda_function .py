"""
Một hàm lambda là một hàm ẩn danh nhỏ. 
Một hàm lambda có thể nhận bất kì số lượng đối số ngào nhưng chỉ cso thể có 1 biểu thức 
"""
 # tên hàm      lambda- đối số- expression. = > return về giá trị
kiemTraSoChan = lambda a: (a%2==0)
print(kiemTraSoChan(4))

if kiemTraSoChan(5):
    print("Day la so chan ")
else:
    print("Đây là số lẻ")

tinhtong= lambda a, b: a+b
print(tinhtong(2,5))
