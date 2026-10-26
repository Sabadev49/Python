#project 1
def double(number):
    return 2*number

x=double(2)
print(x)
#project 2
def full_name(name,last_name):
    return name + last_name
name=full_name("saba ","sedighi nasab")
print(name)
#pro 3
def is_even(num):
    if num %2==0:
        return True
    else:
        return False
x=is_even(5)
print(x)
#pro 4
def max_num(num1,num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
t=max_num(7,7)
print(t)
#boss fight
def calculate_discount(price):
    if price  > 500000:
        return price - price/10
    else:
        return price
final_price=calculate_discount(700000)
print(final_price)
#super boss
def square(num):
    return num*num
def cube(num):
    return num*num*num
def average(num1,num2):
    return (num1+num2)/2
a=square(2)
b=cube(2)
c=average(6,8)
print(a)
print(b)
print(c)



























    
    
