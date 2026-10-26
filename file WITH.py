with open("myname.txt", "w") as file:
    file.write("saba\n")
    file.write("Python Student")
#-----------------------------------
with open("note.txt","w") as file:
    file.write("today i learnsd file")
with open("note.txt","r")as file:
    print(file.read())
#-----------------------------------
with open ("shopping.txt","w") as file:
    file.write("milk\n")
with open("shopping.txt","a") as file:
    file.write("\nbread")
    file.write("\negg")
with open ("shopping.txt","r") as file:
    print(file.read())
#-----------------------------------
user_name=input("Enter your name: ")
with open("user_name","w") as file:
    file.write(user_name)
with open("user_name","r") as file:
    print(file.read())
#-----------------------------------
user_name=input("Enter your name: ")
user_age=int(input("Enter your age: "))
major=input("Enter your major: ")
with open("student.txt","w") as file:
    file.write(f"Age : {user_age}")
    file.write(f"\nName : {user_name}")
    file.write(f"\nMajor : {major}")
with open ("student.txt","r") as file:
    print(file.read())
#-----------------------------------
task=input("write todays note: ")
with open("diary.txt","a") as file:
    file.write(f"\n{task}")
#----------------------
with open("hello.txt","w") as file:
    file.write("Hello Python")
with open("hello.txt", "r") as file:
    print(file.read())
    
