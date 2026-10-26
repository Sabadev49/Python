# project 1

age=int(input("enter your age:"))
if age < 13:
    print("kid")
elif 13< age <18:
    print("teen")
elif age >= 18:
    print("adult")
# project 2
number=int(input("enter a number :"))
if number > 0:
    print(" the number is +")
elif number< 0 :
    print("the number is - ")
else:
    print("its zero")
# project 3
grade=int(input("enter grade :"))
if grade >90:
    print("grate!")
elif 75<grade<90:
    print("normal")
elif 75<grade<50:
    print("not bad")
elif grade<50:
    print("bad")
# project 4
height =int(input("Enter your height: "))
age=int(input("Enter your age: "))
with_mom= True
if height < 120:
    print("NO")
elif height > 120 and age<12 :
    if with_mom:
        print("NO, come with mom")
else:
    print("OK")
# project 5
coffee_size=input("ENTER your favorite coffee size(small,medium,large):")
if coffee_size == "small":
    price = 10
elif coffee_size == "medium":
    price = 15
elif coffee_size == "large":
    price = 20
esperco=input("do u want esperco?(yes,no): ")
if esperco == "yes":
    price=price+5
milk=input("do u want milk?(yes,no): ")
if milk == "yes":
    price= price + 3
print("the price of your cofee is:",price)
# project 6
password=1234
balance=590000
passwords=int(input("Enter your password:"))
if passwords != password:
    print("FALSE")


print("1.show balance\n", "2.vajh\n,","3.bardasht\n","4.exit")
#project 6
price=input("enter price: ")
if price < 100000:
    price=price
elif 100< price <300:
    price= price - price / 10
elif 30< price < 500:
    price = price - price / 20
elif price > 500000:
    price = price - price/30

print(price)














    
    
    
    
    
    
    
    
    
    











































