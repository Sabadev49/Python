#mini exam
# project 1
def check_name(name):
    if name.startswith("s") :
        print("Hello!")
    else :
        print( "try again")
check_name("saba")
check_name("mobina")
# project 2
name ="saba sedighi nasab"
print(name.split())
print(name.split()[0])
print(name.title())
print(name.count("a"))
# project 3
names=["ali","saba","roya","diana"]
for name in names:
    if name.startswith("s"):
        print(f" {name} ⚜ VIP")
    else:
        print(name)
# project 4
prices=[]
def discount(price):
    if price > 500000:
        price=price-(price*10/100)
        prices.append(price)
    else:
        return price
for price in prices:
    print(price)
discount(900000)
# project 5
password=63792
user_name="saba"
guess=int(input("enter your password: "))
while password != guess:
    guss=int(input("enter your password: "))
    if password == guess:
        print(f"welcome {name}")
print(user_name.title())
# project 6
names="ali","saba","roya","diana"
print(names.split(","))
for name in names:
    print(name.title())
    if name.startswith("a") >= 2:
        print("beatifull name")
# project 7



























        





































        