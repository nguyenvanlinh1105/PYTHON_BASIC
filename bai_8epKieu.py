# chuyển đổi ngầm định  , chuyển đổi tường minh 

a = 6 
b = 2.5 
a = a*b
print(a)
print("Kiểu dữ liệu của a là: ",type(a))# ép kiểu ngầm định 
# để ép kiểu tránh mất dữ liệu thì python luôn đấy phép toán lên float 
print(type(b))


#           ÉP KIỂU TƯỜNG MINH 
n = 100
m="200"
#print(n+m)
print(str(n)+m)
print(n+int(m))

