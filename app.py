#projecd 1
age=int(input("enter your age:"))
if age >= 18:
    print("u can vote")
else:
    print("u cant vote")
print("-"*30)
#project 2
number=int(input("enter a number"))
    if number> 0 :
    print("positive")
    elif number < 0:
    print("negetive")
    elif number == 0: #or else:
        print("zero")
#project 3
average=int(input("enter your average"))
if average > 17:
    print("excelent")
elif 12< average <17:
    print("Good")
elif average < 12:
    print("Failed")
#project 4
num1 =int(input("enter a number: "))
num2 =int(input("enter a number: "))
if num1> num2:
    print("the first number is bigger")
elif num1<num2:
    print("second number is bigger")                                                   
elif num1 == num2:
    print ("equal")
    
#project 5
password=input("enter the password")
if password == "python123":
    print("welcome!")
else:
    print("wrong password")
#project 6
    price=int(input("enter the price:"))
if price > 500000 :
    new_price=price-price/10
    print("new price: {new_price}")
else:
    print(price)
#boss fight
age=int(input("Enter your age:"))
money=int(input("Enter your money:"))
if age>18 and money > 500000:
    print("u can buy a ticket")
elif age > 18 and money < 500000:
    print("not enough money")
elif age < 18 :
    print("u are underage")
    
    
    