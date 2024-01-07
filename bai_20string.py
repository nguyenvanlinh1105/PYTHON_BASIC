a = "linh nguyen"
print(type(a))
# nối chuỗi 
lastName ="Nguyen Van"
firstName = "Linh"
print(lastName+" "+firstName)



# Chuỗi nhiều dòng
chuoi_nhieuDong="""
chuoinhieudong
dong1
dong2
dong 3

"""
print(chuoi_nhieuDong)
chep_phat='em hứa làm bài tập đầy đủ\n '
chep_phat_10 = chep_phat*10
print(chep_phat_10)

# hàm in /constaint kiểm tra tồn rại 
chuoi_1="Nguyen van Linh"
chuoi_2="Nguyen"
chuoi_3="y"
if chuoi_2 in chuoi_1:
    print("Chuoi 2 là chuỗi con cua chuoi 1")
else:
    print("Chuoi 2 khong phải la chuoi con cua huoi 1")

if chuoi_2 in chuoi_3:
    print("Chuoi 2 là chuỗi con cua chuoi 3")
else:
    print("Chuoi 2 khong phải la chuoi con cua chuoi 3")


# viets hoa toàn bộ chuỗi
s="hôm nay trời đẹp quá"
s = str.capitalize(s)
print(s)
# viets hoa toàn bộ chuôi 
s=str.upper(s)
print(s)
# chuoix viet thường 
s = str.lower(s) 
print(s) 

# tìm và đếp số lượng chuỗi con 
s = 'lập trình là xu hương hiện nay bạn nên học lập trình python'

print(s.find("trình")) # trả về vị trí đầu tiên nếu tìm thấy và trả về -1 nếu không tìm thấy 
print("Số lương 'trình' trong s là ",s.count("trình"))

# thay thế 
s=s.replace("python","PYTHON")
print(s)

# cắt chuỗi thành mảng 
list = s.split(" ")
print(list)

# in ra 





