# vòng lặp for 
# cú pháp :
for i in range(10):
    print(i)
# tinh tong tu 0 đen n

n = int(input("Nhap vao n"))
tong =0
for i in range(n):
    tong+=i
print(tong)

# Vòng lặp for,có bước tăng tùy chỉnh
for i in range(0,10,2):# bắt đầu, kết thúc, bước chạy. 
    print(i)
for i in range(10,0,-4):
    print(i)

print("lặp qua list để in ra ")
list =[1, 2, 3,4, 'Linh']
for it in list:
    print(it)


# cách 2: duyet phần tử theo vi tri
for i in range(len(list)):
    print(list[i])