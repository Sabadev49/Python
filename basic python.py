#Qustion 1
number=int(input("Enter a number: "))
if number %2 == 0:
    print("even")
else:
    print("odd")
#Qustion 2
age=int(input("Enter your age :"))
if 13<age<18:
    print("accpted")
else:
    print("rejected")
#Qustion 3
for i in range(1,30):
    if i % 5 == 0:
        print(i)
#Qustion 4
for i in range(1,20):
    if i == 12:
        continue
    print(i)
#Qustion 5
for i in range(1,100):
    if i == 63:
        break
    print(i)
#Qustion 6
number =int(input("Enter a number :"))
while number > 0 :
    number =int(input("Enter a number :"))
    if number < 0 :
        print("bye")
#Qustion 7
numbers=[5,8,3,9,1]
numbers.append(7)
numbers.remove(3)
remove_item=numbers.pop(-1)
print(numbers)
#Qustion 8
person={
    "name":"saba",
    "age" : 20
    }
person["city"]="Arak"
print(person["city"])
#Qustion 9
password="python"
user_password=input("Enter your password :")
while user_password != password:
    user_password=input("Enter your password :")
    if user_password == password:
        print("welcome ")
#Qustion 10
for i in range(5):
    grade=int(input("Enter your grade: "))
    if grade < 10:
        print("Failed")
    elif grade >= 10:
        print("passed")
#super boss
user_name=input("Enter your name: ")
password=5398431
user_password=int(input("Enter your password: "))
while user_password != password:
    user_password=int(input("Enter your password: "))
    if user_password == password:
        for i in range(5):
            print(user_name)
            for i in range(0,20,2):
                print(i)
        
        
        
        
        














    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    

