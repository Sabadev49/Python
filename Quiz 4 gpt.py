def discount(price):
    if price > 500000:
     final_price=price-(price*15/100)
     return final_price
    else:
        return price 
discount(900000)    
#pro 2
grades=[8,12,19,7,15,20]
for grade in grades:
   if grade >= 10:
      print("grade")
#pro 3
try:
   plus_number=int(input("enter a number: "))
   while plus_number < 0:
      plus_number=int(input("enter a number: "))
except:
   print("Warning")
print(plus_number)
#pro 4
def check_email(email):
   if email.startswith("@"):
      print("valid email")
   else:
      print("invalid email")
#pro 5
student={
   "name":"saba",
   "age": 20,
   "major":"accounting"
}
student["grade"]=19.5
for i in student:
   print(student.items())
#boss fight1
names=["ali","saba","reza","sam"]
for name in names:
   if name.startswith("s"):
      print(name)
#boss fight2
def calculator(num1,num2,operation):
   if operation == "+":
        return num1+num2
   elif operation == "-":
      return num1-num2
   elif operation == "*":
      return num1*num2
   elif operation == "/":
      return num1/num2
print(calculator(5,6,"+"))
#nightmare challenge
name="saba"
password="python123"
print("wecome u most enter true name and true password. if 3s wrong, the computher bloked.")
user_password=input("enter your password: ")
user_name=input("enter your name: ")
attempts=0
while user_name != name and user_password != password:
    user_password=input("enter your password: ")
    user_name=input("enter your name: ")
    if user_name != name:
       print("wrong")
    elif name == user_name and user_password != password:
       print("wrong password")
    elif user_password == password and user_name == name:
       print("welcome saba ❤")
       if attempts == 3:
          print("account locked")
          break
       attempts= attempts + 1
       
   
   