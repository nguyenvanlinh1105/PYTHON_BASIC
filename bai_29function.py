# function 
"""
Định nghĩa hàm là một khối lệnh, chỉ chạy khi được khai báo 
- Truyền dữ liệu được gọi là tham số vào một hàm.
- Kết quả là một hàm có thể trả về dữ liệu 

* Khai báo hàm trong python, một hàm được định nghĩa bằng từ khóa def:
    Vidu:
    def xinChao():
        print("xin chào Linh Nguyen");
Gọi hàm 
    xinChao() -> hàm được hoạt động 

ĐỐI số(Arguments) 
    _ hàm co thể nhận vào các tham số :
        def xinChao(hoVaTen):
            print("Tên của tôi là:" +hoVaTen)
    - hàm có thể nhận nhiều đối số :

        
"""
def xinchao(hoten):
    print("Xin chào bạn: "+hoten)

xinchao("Linh Nguyen")


# khi không xác định được đối số, chúng ta có thể sử dụng dấu * 

def thoiKhoaBieu(*monHoc):
    print("Môn 1: "+monHoc[0])
    print("Môn 2: "+monHoc[1])

thoiKhoaBieu("Toán", "Lí", "Hóa", "Văn")


def tinhTong(*giaTri):
    sum = 0
    for x in giaTri:
        sum+=x
    print(sum)

tinhTong(2, 4)
tinhTong(2, 3, 4, 5,6, 7)

# truyền nhiều đối số thông qa tên :
def xinchao(**ten):
    print("Xin chào: "+ten["ten"])
xinchao(ten ="Linh", chuLot="Văn", ho='Nguyễn')

# sử dụng từ khóa return 
def tinhTich(*giaTri):
    tich=1
    for x in giaTri:
        tich*=x
    return tich
x =tinhTich(3, 2, 5,1)

print("Tich la:"+str(x))


# bài tập : Tìm USCLN của hai số a và b phương pháp trừ dần 

def USCLN(a, b):
    while(a!=b):
        if(a>b):
            a =a-b
        else:
            b = b-a
    return a
x = USCLN(21, 7)
print("Ước chung lớn nhât: "+str(x))


# phương pháp oclid
def USC(a, b):
    while a % b != 0:
        r = a % b
        a = b
        b = r
    return b
x = USC(11, 121)
print("USC:"+str(x))


# nhập vào một dãy số (n) từ bàn phím, sau đó tính tổng 
# Yêu cầu xây dựng các hàm 
# nhập(n, list_number)
#tinhTong
def nhap(n, my_list):
    for i in range(n):
        x = int(input("Nhập số thứ {}:".format(i + 1)))
        my_list.append(x)

n = int(input("Nhập bao nhiêu số: "))
my_list = []
def tinhTong(n, my_list):
    sum = 0
    for x in my_list:
        sum+=x
    return sum

nhap(n, my_list)
x = tinhTong(n,my_list)
print("tong day so là: "+str(x))


