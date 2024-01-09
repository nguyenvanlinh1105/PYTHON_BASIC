"""
Một hàm lambda là một hàm ẩn danh nhỏ. 
Một hàm lambda có thể nhận bất kì số lượng đối số ngào nhưng chỉ cso thể có 1 biểu thức 
"""
import math
 # tên hàm      lambda- đối số- expression. = > return về giá trị
kiemTraSoChan = lambda a: (a%2==0)
print(kiemTraSoChan(4))

if kiemTraSoChan(5):
    print("Day la so chan ")
else:
    print("Đây là số lẻ")

tinhtong= lambda a, b: a+b
print(tinhtong(2,5))


# ví dụ về sử dụng lambda function trong các function


def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))



def tinhTich(n):
   return lambda a: a **n

hamnu2 = tinhTich(2)
hamnu3 = tinhTich(3)
hamnu4 = tinhTich(4)
print(hamnu2(2))
print(hamnu3(2))
print(hamnu4(2))


