s = ""
n =int(input("Nhap n"))
while(n>0):
    s= str(n%2)+s
    n=n//2
print(s)