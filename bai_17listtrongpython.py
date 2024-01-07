# Kiểu dữ liệu list :
"""
List:(Danh sách) là một chuỗi các mục có thứ tự. Nó là một trong những kiểu dữ liệu được sử dụng nhiều nhất và rất linh hoạt. tất cả các mục trong danh sách không phải cùng loại. 
Khai báo một danh sách khá đơn giản, các mục được phân tách bằng dấu phẩu đặt trong dấu ngoặc 
"""

listEmpty=[]# đây là một list 

list2= list # tạo ra một đối tương list2 
print(list2)

# tạo ra list có dư liêu 
list3 = ['red','green','orange']
print(list3)

Students =['An','Binh','Ngan','Vi']


# laay ra theo dia chi index 0->n
print(Students[1])

print(Students[:]) # lấy tất cả

# lấy theo đoạn[1:3]
print(Students[1:4])

#Them phần tử vào list 
Students.append("PHa")
Students.insert(2,"Thành")
print(Students[:])

Students[len(Students):]=['Thành']
print(Students)

Students[len(Students):]=['Thành']

# số lượng phần tử có trong list 
print(len(Students))

print('Dem Vi:', Students.count("Thành"))
print(Students)



# Xóa 
Students.remove("Vi")# chỉ xóa 1 vị trí đầu tiên đc tìm thấy 
print(Students)

# Kiểm tra phần tử tồn tại
print(Students.__contains__("Vi"))

if Students.__contains__("Thành"):
    Students.remove("Thành")
# hoặc 
if "An" in Students:
    Students.remove("An")
print(Students)


# Xóa phần tử ra khỏi list bảng index -LIFO
Students.pop(1)
print(Students) 


# Đảo ngược list 
Students.reverse()
print(Students)
# Sắp xếp lại theo đúng thứ tự


# Sắp xếp thuận
Students.sort()
print(Students)

#Sắp xếp ngược 
Students.sort(reverse=True)
print(Students)

#chen
Students.insert(1,'Linh')
print(Students)
# Xóa dữ liệu all in
Students.clear()
print(Students)