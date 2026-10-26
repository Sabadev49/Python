#project 1
for i in range(10):
    grade=int(input("enter your grade:"))
    if grade < 10:
        print("failed")
    elif grade >= 10:
        print("passed")
#project 2
password=5398431
for i in range(3):
    user_password=int(input("enter your password:"))
    if user_password == password:
        print("welcome !")
    if i == 3:
        break
print("your account i s locked")
    
