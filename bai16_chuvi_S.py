import math
r = int(input("Nhap bán kính r: "))
c = 2*math.pi*r
print("Chu vi hinh tron là: ", c)

s = math.pi*math.pow(r,2)
print("Dien tich hinh tron la: ",s)

a =int(input("Nhap canh a"))
b =int(input("Nhap canh b:"))
c =int(input("Nhap canh c"))

tamgiac = a+b+c
nuac= (tamgiac)/2
dientich = math.sqrt(nuac*(nuac-a)*(nuac-b)*(nuac-c))

print("Chu vi tam giac là: ",tamgiac)
print('Dien tich tam giac la:', dientich)



