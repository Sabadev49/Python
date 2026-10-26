class dog:
    def __init__(self,name):
        self.name=name
    def bark (self):
        print(f"{self.name} says Woof!")
dog1=dog("Rocky")
dog1.bark()
#p1
class Book:
    def __init__(self,title):
        self.title=title
    def show(self):
        print(f"Book : {self.title}")
Book1=Book("python")
Book1.show()
#p2
class Car:
    def __init__(self,brand):
        self.brand=brand
    def drive(self):
        print(f"{self.brand} is driving...")
Car1=Car("BMW")
Car1.drive()
#p3
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"Name : {self.name}\n Age : {self.age}")
student1=student("saba",22)
student1.show()
#p4
class Cat:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def introduce(self):
        print(f" I am {self.name}\n my color is {self.color}")
cat1=Cat("luna","brown")
cat1.introduce()
#p5
class Phone:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def info(self):
        print(f" brand: {self.brand}\n price : {self.price}")
Phone1=Phone("samsung",5400000000000)
Phone1.info()


