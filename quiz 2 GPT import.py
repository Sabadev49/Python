#quiz gpt
from random import randint
print(randint(1,100))
#project 2
colors=["red", "blue", "green", "purple"]
from random import choice
secret_color=choice(colors)
print(secret_color)
#project 3
try:
    number= int(input("enter a number:"))
    from math import pow
    print(pow(number))
except:
    print("invalid")

try:
    number= int(input("enter a number:"))
    if number %2==0:
        print("even")
    else:
        print("odd")
except:
    print("invalid")
#project 4

#project 5
# 8
#project 6
from random import randint
number=randint(1,20)
print(number)
#boss fight
try:
    from random import randint
    select_number=randint(1,5)
    user_number=int(input("enter a number: "))
    if select_number == user_number:
        print("winner")
    else:
        print("try again")
except:
    print("pls enter a number.")
print(f"the number is: {select_number}")
#super boss
