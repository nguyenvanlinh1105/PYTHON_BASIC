# BIẾN, HẰNG SỐ, VÀ TỪ KHÓA TRONG PYTHON 

# BIẾN : là vị trí được đặt tên, để lưu trữ dữ liệu trong bộ nhớ, giá trị có thể thay đổi trong quá trình thực hiện chương trình
 
y = 5
y = 89 # ghi đè giá trị y ban đầu
print("Giá trị của y là :", y)
# dùng một dấu bằng gán nhiều giá trị 
x, y, z= 1, 424,'Linh Nguyen'
print(x, y, z)

# Gán giá trị cho nhiều biến và có giá trị giống nhau 

t = k = r='Linh Nguyen'
print(t, k, r, sep='-')


#                   HẰNG SỐ 


# HẰNG : là ví trí được đặt tên, để lưu trữ dữ liệu trong bộ nhớ, không thể thay đối trong quá trình làm việc 
# trong python thực sự không có hằng số : hằng số thường được khai bao và gán trong một mô-đun và người dùng hạn chế không thay đổi giá trị của nó. Ở đây, mô-đun là một tệp mơii chứa các biến, hàm, v.v. được nhập vào tệp chính. Bên trong mô-đen các hằng số được viết bằng tất cả chữ cái in hoa và dấu gạch dưới ngăn cách các từ 

#ví dụ : 
PI = 3.14
print(PI)
PI=3.1415
print(PI)

import math
print(math.pi)


"""
 # Cách dặt tên biến và hằng số : Sử dụng các chữ cái (a-z), (A-Z) các con số (0-9), dấu gạch dưới_ để đặt tên cho biến hoặc hằng số 
    - Không bắt đầu bằng chữ số, và các từ khóa đặt tên biến 
 # Ví dụ : 
        content ="Học lập trình"  => tên biến nên co ý nghĩa và phù hợp với nội dung cần chứa 

        full_name="Nguyễn Văn Linh"
"""







