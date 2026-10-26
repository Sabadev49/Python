#zip()
names=["Ali","Saba","Sara"]
ages=[21,20,19]
for name,age in zip(names,ages):
    print(name,age)
#p2
products=["mouse","keyboard","monitor"] 
prices=[500000,1200000,800000]
print(list(zip(products,prices)))
#p3
cities=["Tehran","Arak","Tabriz"]
population=[900000,600000,1700000]
for city,pop in zip(cities,population):
    print(f"{city} has {pop} people")
#p4
students=["Ali","Saba","Sara"]
grades=[18,20,17]
for student,grade in zip(students,grades):
    if grade >= 18:
        print(student,grade)
#boss fight
names=["Ali","Saba","Sara"]
ages=[21,20,19]
majors=["math","accounting","computer"]
for name,age,major in zip(names,ages,majors):
    print(f"{name}|{age}|{major}")
#------------------------------------------
with open("hello.txt","w") as file:
    file.write("Hello Python")
with open("hello.txt", "r") as file:
    print(file.read())
#p2
names=["Ali","saba","roya"]
grades=[18,20,17]
for name,grade in zip(names,grades):
    print(name,grade)
#p3
products=["mouse","keyboard","monitor"]
prices=[500000,1200000,800000]
stocks=[15,8,3]
for product,price,stock in zip(products,prices,stocks):
    print(f"{product}|{price}|{stock}")
#p4
user_name=input("enter your name: ")
user_age=int(input("enter your age:"))
with open("information.txt","w") as file:
    file.write(user_name)
    file.write(f"\n{user_age}")
with open("information.txt","r") as file:
    print(file.read())
#boss fight
students=["Ali","Saba","Sara","Reza"]
grades=[18,20,15,9]
majors=["Math","Accounting","Computer","Physics"]
print(list(zip(students,grades,majors)))
for name,grade in zip(names,grades):
    if grade>=18:
        print(f"{grade},{name}")
with open ("students.txt","w") as file:
    for student,major,grade in zip(students,majors,grades):
        file.write(f"{student}|{major}"|{grade})
with open("student.txt","r")as file:
    print(file.read())
#mini nightmare
name1=input("enter a name:")
name2=input("enter a name:")
name3=input("enter a name:")
num1=input("enter a number:")
num2=input("enter a number:")
num3=input("enter a number:")
phone_numbers=[]
names=[]
phone_numbers.extend([num1,num2,num3])
names.extend([name1,name2,name3])
result=zip(phone_numbers,names)
print(list(result))
with open("contacts.txt","w") as file:
    file.write(f"{name1}:{num1}")
    file.write(f"{name2}:{num2}")
    file.write(f"{name3}:{num3}")
with open("contacts.txt","r")as file:
    print(file.read())