#project 1
try:
    number=int(input("Enter a number:"))
    print(number)
except:
    print("invalid number")
#project 2
try:
    user_age=int(input("enter your age:"))
    print(user_age)
except:
    print("please enter a number")
#project 3
try:
    def plus(num1,num2):
        return num1 + num2
    num1=int(input("Enter first number:")) 
    num2=int(input("Enter second number:"))
except:
    print("Warning")
#project 4
try:
    number=int(input("Enter a number: "))
    if number %2 == 0:
        print("the number is Even.")
    else:
        print("the number is odd.")
except:
    print("warning")