numbers=[5,10,15,20]
new_numbers=map(lambda num: num*3,numbers)
print(list(new_numbers))
#p 2
names=["ali","saba","roya"]
upper_names=map(lambda name: name.upper(),names)
print(list(upper_names))
#p 3
numbers=[5,8,10,11,14]
even_numbers=filter(lambda num: num%2==0,numbers)
print(list(even_numbers))
#p4
posoeneg=lambda x: "postive" if x>0 else "negative"
print(posoeneg(9))
#p5
prices=[100,250,400,800]
new_prices=map(lambda price: price-(price*20/100) if price > 300 else price,prices)
print(list(new_prices))
#p6 
grades=[8,12,20,17,5]
passed=filter(lambda grade: grade>= 10,grades)
print(list(passed))
#p7
bigger=lambda num1,num2: num1 if num1>num2 else num2
print(bigger(2,6))
#p8
words=["python","c","java","javascript","go"]
words2=filter(lambda word: len(word) > 4 , words)
print(list(words2))
#p9 nightmare
students={
    ("Ali",18),
    ("saba",20),
    ("reza",20),
    ("roya",17),
    ("sara",19)
}
grade_A=filter(lambda student: student[1]>=18 ,students)
print(list(grade_A))
#p10
lists=map(lambda student: f" Student : {student[0]}",students)
print(list(lists))
#p11
numbers=[2,5,8,11,14,17,20]
even_numbers=filter(lambda num: num%2==0,numbers)
square=map(lambda num: num**2, even_numbers)
print(list(square))
