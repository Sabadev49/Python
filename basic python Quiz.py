#p1
evenorodd=lambda num: "Even" if num%2 == 0 else "odd"
print(evenorodd(4))
#p2
bigger_num=lambda num1,num2: num1 if num1> num2 else num2
print(bigger_num(9,2))
# --------------------------
# p3
fifth=lambda number : number *5
print(fifth(9))
#p4
threenum=lambda num1,num2,num3 : num1+num2+num3
print(threenum(1,2,3))
#p5 
Remainder=lambda num1,num2 : num1% num2
print(Remainder(89,6))
#p 6
NegorPos=lambda number: "positive" if number>0 else "negative"
print(NegorPos(-10))
# p 7
raise5=lambda num:"yes" if num%5 == 0 else "no"
print(raise5(77))
#p8
lower_num=lambda num1,num2: num1 if num1< num2 else num2
print(lower_num(8,9))
#p9 
stringlenghth= lambda string: "long" if len(string)>5 else "short"
print(stringlenghth("saba sedighi nasab"))
#p 10
grade=lambda grade : "A" if grade>= 18 else "B" if grade<=15 else "B"
print(grade(19))
#p 11
odd_or_even=lambda num: num**2 if num%2==0 else num**3
print(odd_or_even(9))
#p12
bigger=lambda num1,num2,num3: num1 if num1>num2 and num1>num3 else num2 if num2>num1 and num2> num3 else num3
# p 13
login=lambda age: "access" if age>=18 else "denied"
print(login(16))
# ------------------------------------------
#p1 
pos_or_neg=lambda num: "positive" if num>0 else "zero" if num == 0 else "negative"
#p2
grade=lambda grade: "A" if grade>=18 else "B" if grade>=15 else "C" if grade>= 10 else "F" 
#p3
age=lambda age : "senior" if age >=60 else "Adult" if 18<=age<60 else "child"
#p4
number=lambda number : "even positive" if number%2==0 and number>0 else "even negative" if number%2==0 and number<0 else "odd"
# p 5 boss fight
bigger_number= lambda num1,num2,num3:num1 if num1>num2 and num1>num3 else num2 if num2>num1 and num2>num3 else num3 if num3>num1 and num3>num2 




































