#project 1
def check_discount(price):
    if price > 300000:
        price=price-(price*20/100)
        return price
    else:
        return price
print(check_discount(900000))
#project 2
names=["saba","ali","sara","reza","sam"]
for name in names:
    if name.startswith("s"):
        print(name.upper())
#project 3
sentence=input("enter a sentence: ")
w=sentence.count("a")
print("the number of 'a' in your sentence:",w)
print(sentence.title())
if sentence.startswith("H"):
    print("yes. the sentence started with H.")
#proj 4
student={
    "name":"saba",
    "age":20,
    "grade":19.5
        }
print(student.items())
#proj 5
try:
    number1=int(input("enter a number1:"))
    number2=int(input("enter a number2:"))
    print(number1+number2)
except:
    print("invalid input")
#proj 6
colors=["red","blue","green","purple"]
user_color=input("enter a color: ")
from random import choice
choice_color=choice(colors)
if user_color == "purple":
    print("lucky color!")
else:
    print(f"the color is:" ,{choice_color})
#proj 7
true_user_name="saba"
true_password="python123"
true_user_name="saba"
user_name=input("enter your user name: ")
user_password=input("enter your password: ")
attempts=0

while user_name != true_user_name or user_password != true_password:
    user_name=input("enter your user name: ")
    user_password=input("enter your password: ")
    if attempts == 3:
        print("account locked.")
        break
    elif user_name == true_user_name and user_password == true_password:
        print("welcome")
    attempts=+1
#proj 8
    def calculator(num1,num2,operation):
        if operation == "+":
          return num1+num2
        elif operation == "-":
         return num1-num2
        elif operation == "*":
          return num1*num2
        elif operation == "/":
            return num1/num2
try:
    print(calculator(5,6,"+"))
except:
   print("invalid operation.")


