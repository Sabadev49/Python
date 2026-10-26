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
#real proj
#------------------------------
class Counter:
    def __init__(self):
        self.number=0
    def show_num(self):
        print(self.number)
    def add_one(self):
        self.number+=1
counter=Counter()
counter.show_num()
counter.add_one()
counter.show_num()
counter.add_one()
counter.show_num()
#p2
class Player:
    def __init__(self,name):
        self.name=name
        self.health=100
    def damage(self):
        if self.health == 0:
            print("Game over!")
        else:
          self.health-=10
    def show_health(self):
        print(f" {self.name}:{self.health}")
player1=Player("saba")
player1.damage()
player1.damage()
player1.show_health()
#p3
class Glass:
    def __init__(self):
        self.water=5
    def fill(self):
        self.water+=1
    def show(self):
        print(self.water)
water=Glass()
water.fill()
water.fill()
water.show()
#bank project 
class Bank:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        if amount <= self.balance:
           self.balance-=amount
        else:
            print("insufficient balance")
    def deposit(self,amount):
        self.balance+=amount
    def show_balance(self):
        print(self.balance)
person1=Bank(300)
person1.deposit(200)
person1.withdraw(100)
person1.show_balance()
#shopping list
class Shop:
    def __init__(self):
        self.items=[]
    def add(self,item):
        self.items.append(item)
    def remove(self,item):
        if item in self.items:
          self.items.remove(item)
        else:
            print("not found")
    def show_list(self):
        print(self.items)
list1=Shop()
list1.add("egg")
list1.add("water")
list1.add("chicken")
list1.remove("egg")
list1.remove("milk")
list1.show_list()
#Library
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"the {book} is not in books")
    def show_list(self):
        print(self.books)
book1=Library()
book1.add_book("food with me")
book1.show_list()
#counter
class Counter:
    def __init__(self):
        self.count=0
    def increase(self):
        self.count+=1
    def decrease(self):
        if self.count > 0:
            self.count-=1
        else:
            print("Eror!")
    def show(self):
        print(self.count)
count1=Counter()
count1.increase()
count1.increase()
count1.increase()
count1.increase()
count1.decrease()
count1.show()
#car
class Car:
    def __init__(self,brand):
        self.fuel=50
        self.brand=brand
    def refuel(self,amount):
        self.fuel+=amount
    def drive(self):
        if self.fuel <= 0:
            print("Out of fuel!")
        else:
            self.fuel-=10
    def show(self):
        print(f"the{self.brand} fuel is : {self.fuel}")
car1=Car("BMW")
car1.refuel(200)
car1.drive()
car1.show()
#p 1----------------------
class Book:
    def __init__(self,title,new_pages):
        self.title=title
        self.pages=new_pages
    def change_pages(self,new_pages):
        self.pages.append(new_pages)
    def show(self):
        print(f"{self.title} : {self.pages}")
#p2
class Phone:
    def __init__(self,brand):
        self.battery=100
        self.brand=brand
    def use(self):
        if self.battery <= 0 :
            print("battery is empty!")
        else:
            self.battery-=20
    def charge(self):
        self.battery=100
    def show(self):
        print(self.battery)
phone1=Phone("samsung")
phone1.use()
phone1.show()
#boss fight
class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def increase(self,amount):
        if self.grade == 20:
            print("Maximum grade is 20")
        else:
            self.grade+=amount
    def decrease(self,amount):
        if self.grade < 0:
            print("Minimum grade is 0")
        else:
            self.grade-=amount
    def show(self):
        print(f"{self.name}:{self.grade}")
student1=Student("saba",17)
student1.increase(2)
student1.decrease(5)
student1.show()
#Inheritance 
class Person:
    def __init__(self,name):
        self.name=name
    def introduce(self):
        print(f"Name : {self.name}")
class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade   
student1=Student("saba",19)
student1.introduce()
#p2
class Person:
    def __init__(self,name):
        self.name=name
class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
    def introduce(self):
        print(f"I am {self.name} sub : {self.subject}")
    
teacher1=Teacher("somayeh","math")
teacher1.introduce()
#----------------------------------
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f"{self.name} makes a sound")
class Bird(Animal):
    def __init__(self, name,color):
        super().__init__(name)
        self.color=color
    def fly(self):
        print(f"{self.name} is flying")
bird1=Bird("jojo","blue")
bird1.sound()
bird1.fly()
#p2
class Vahicle:
    def __init__(self,brand):
        self.brand=brand
    def show_brand(self):
        print(f"Brand : {self.brand}")
class Bike(Vahicle):
    def __init__(self,brand,gears):
        super().__init__(brand)
        self.gears=gears
    def show_gears(self):
        print(f"Gears : {self.gears}")
car1=Bike("BMW",23)
car1.show_gears()
car1.show_brand()
#p3
class Empoloyee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_salary(self):
        print(f"{self.name}'s salary is {self.salary}")
class Manager(Empoloyee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
    def show_department(self):
        print(f"Department : {self.department}")
person1=Manager("Ali",2000000,"IT")
person1.show_department()
person1.show_salary()
#p4
class Book:
    def __init__(self,title):
        self.title=title
    def show_title(self):
        print(f"Book : {self.title}")
class EBook(Book):
    def __init__(self, title,size):
        super().__init__(title)
        self.size=size
    def download(self):
        print(f"Downloading {self.title}...")
book1=EBook("python","238 kb")
book1.show_title()
book1.download()
#p5
class Person:
    def __init__(self,name):
        self.name=name
    def say_name(self):
        print(f"my name is {self.name}")
class Doctor(Person):
    def __init__(self, name,specially):
        super().__init__(name)
        self.specially=specially
    def work(self):
        print(f"{self.name} is a {self.specially} doctor")
p1=Doctor("saba","brain")
p1.say_name()
p1.work()
#------------------------------
class Person:
    def __init__(self):
        pass
    def introduce(self):
        print("Hello I'm a person")
class Student(Person):
    def introduce(self):
        print("Hello I'm a student")
p1=Person()
p1.introduce()
p2=Student()
p2.introduce()
#-------------------------------------
class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance< amount:
            print("insufficient balance")
        else:
            self.balance-=amount
    def show_balance(self):
        print(f"{self.owner} balance :{self.balance}")
class SavingAccount(Account):
    def __init__(self, owner, balance,interest):
        super().__init__(owner, balance)
        self.interest=interest
    def add_interest(self):
        self.balance+=self.balance*self.interest/100
person1=SavingAccount("saba",7000000,10)
person1.withdraw(300)
person1.deposit(200)
person1.add_interest()
person1.show_balance()


    










































