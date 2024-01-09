# Bài tập OOP 
# phân biệt method,  attribute 
# Lớp , đối tượng, thuộc tính và phương thức 
"""
1. Object 
2. Class 
3. Method
4. Inheritance
5. Polymorphism
6. Encapsulation 
7. Data 
"""
class SimpleClass :
    # attribute 
    i = 2
    # hàm constructor , _init_
    def __init__(self):
        self.j = 20
    
    def printJ(self):
        print(self.j)
    @staticmethod
    def hiStatic(name):
        #Instance atrribute 
        print("Hi",name)

objectA = SimpleClass()
objectA.printJ()
print(objectA.i)
# gọi hàm static 
print(SimpleClass.hiStatic("Linh Nguyễn"))


# thay đổi giá trị của thuộc tính
objectA.i = 100
objectA.j=500
print(objectA.i)
objectA.printJ()




class Car :
    # constructor
    def __init__(self) :
        self.name ="Linh"
    # method
    def hello(self):
        print("Hello "+self.name)
    # static method
    @staticmethod
    def hi(name):
        print("Hi"+name)

print(Car.hi("Linh Nguyễn"))
# thay đổi 
