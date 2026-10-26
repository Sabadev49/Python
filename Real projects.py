#real projects
name=input("name : ")
age=input("age : ")
major=input("major : ")
grade=float(input("grade : "))
names=[]
names.append(name)
ages=[]
ages.append(age)
majors=[]
majors.append(major) 
grades=[]
grades.append(grade)
for name,age,major,grade in zip(names,ages,majors,grades):
    print(name,age,major,grade)
if grade >= 18:
    print("EXCELENT student.")
with open("student.txt","w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Major : {major}\n")
    file.write(f"Grade: {grade}\n")
with open("student.txt", "r") as file:
    print(file.read())
#=-------------------------------------------
books=input("Enter a book: ")
books_list=[]
books_list.append(books)
while books!= "stop":
    books=input("Enter a book: ")
with open("book.txt","w")as file:
    for book in books_list:
     file.write(book+"\n")
with open("book.txt","r")as file:
    print(file.read())
print(len(books_list))
#real proj 2
products=[
    ("mouse",500000),
    ("keyboard",120000),
    ("monitor",900000),
    ("flash",350000)
]
for x,y in products:
    if y>1000000 :
        print(x)
H=map(lambda product: f"product : {product[0]}",products)
print((list(H)))
#real pro 3
students={
    "Ali":18,
    "Saba":20,
    "Sara":9,
    "Reza":15,
    "Roya":19
}
for key,value in students.items():
    print(f"average : {sum(students.values())/len(students.values())}")
print(max(students.values()))
print(min(students.values()))
passed= filter(lambda value: value>=10,students.values())
print(list(len(passed)))
excelent=filter(lambda value: value >= 18,students.items())
print(list(excelent))