# Nhap dữ liệu 
import math
print("Giải phương trình bậc 2")
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

denta = b*b - 4*a*c

if a==0:
    if b==0:
        if c==0:
            print("Phuong trinh co vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co nghiem duy nhat: ", -c/b)   
else:
    if denta >0:
        x1 = (-b+math.sqrt(denta))/ 2*a
        x2 = (-b-math.sqrt(denta))/ 2*a
        print('phuong trinh co 2 nghiem phan biet: x1={0}, x2={1}'.format(x1, x2))
    else:
        if denta ==0:
            print("Phuong trinh co 1 nghiem kep duy nhat: ",-b/2*a)
        else:
            print("phuong trinh vo nghiem ")

            

        



