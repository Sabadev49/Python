numbers=[5,10,15,20,25]
multiple10=filter(lambda num: num%10==0,numbers)
w=map(lambda num:f"Number : {num}",multiple10)
print(list(w))
#p2 ---------------------------
prices=[100,200,700,900]
bigger500=[price-(price*2/10) for price in prices if price>500]
print(bigger500)
# p3---------------------------
between=lambda num1,num2,num3: num1 if num2<num1<num3 else num2 if num1<num2<num3 else num3
print(between(1,2,3))
# p4---------------------------
names=["ali","saba","sam","roya","sina"]
startS=filter(lambda name: name.startswith("s"),names)
print(list(startS))
# p5---------------------------
numbers=[8,2,15,20,7]
new_numbers=numbers.copy()
new_numbers.sort()
new_numbers.reverse()
print(max(new_numbers))
print(min(new_numbers))
# p6---------------------------
student={
    "name":"saba",
    "age":20,
    "grade":19.5
}
print(student.keys())
print(student.values())
print(student.get("major","not found"))
# p7---------------------------
try:
    number=int(input("Enter a number: "))
    from math import sqrt
    print(sqrt(number))
except:
    print("invailid input")
# boss fight---------------------------
students={
    ("Ali",18),
    ("Saba",20),
    ("Reza",12),
    ("Sara",19),
    ("Roya",8)
}
gradeA=filter(lambda student: student[1]>=18,students)
w=map(lambda student: f"Excelent : {student[0]}",gradeA)
print(list(w))
print(len(list(gradeA)))
# nightmare challenge---------------------------
numbers=[1,2,3,4,5,6,7,8,9,10]
even=filter(lambda num: num%2==0,numbers)
print(list(even))
x=map(lambda num:f"score : {num}")
print(list(x))
# ---------------------------
numi=lambda num: "A" if num%2==0 and num%3==0 else "B" if num%2==0 else "C" if num%3==0 else "D"
print(numi(7842))
