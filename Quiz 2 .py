#mini nightmare
products={
    ("laptop",45000000),
    ("mouse",500000),
    ("keyboard",1200000),
    ("monitor",9000000),
    ("flash",350000)
}
bigger1M=filter(lambda product: product[1]> 1000000,products)
new_list=map(lambda product: f"product : {product[0]}",bigger1M)
print(list(new_list))
products2=[product[0] for product in products]
print(products2)
products2.sort()
print(products)
print(len(list(bigger1M)))
#quiz ---------------------------------------
multiple3= lambda num: "multiple of 3" if num%3==0 else "not multiple" 
print(multiple3(8))
#q 2 ----------------------------------------
numbers=[2,5,8,11,14]
plusten=map(lambda num: num+10 , numbers)
print(list(plusten))
#q 3 -----------------------------------------
numbers=[10,15,20,25,30]
multiple10=filter(lambda num: num%10==0,numbers)
print(list(multiple10))
#q4 -------------------------------------------
names=["ali","saba","sam","roya"]
new_names=[name.upper() for name in names if name.startswith("s")]
print(new_names)
#q5 ----------------------------------------------
grades=[12,18,20,15,8]
print(max(grades))
print(min(grades))
print(len(grades))
averege=sum(grades)/len(grades)
print(averege)
#q 6 --------------------------------------------
numbers=[4,1,9,6]
new_numbers=numbers.copy()
new_numbers.sort()
new_numbers.reverse()
print(new_numbers)
#q7 -------------------------------------
def check_discount(price):
    if price >500:
        final_price=price-(price*15/100)
        return final_price
    else:
        return price
check_discount(900)
#boss fight---------------------------------------
students={
    ("ali",18),
    ("saba",20),
    ("reza",12),
    ("sara",19),
    ("roya",9)
}
passed=filter(lambda student: student[1]>10,students)
welcome=map(lambda student: f"Welcome {student[0]},passed")
print(len(passed))
#nightmare boss--------------------------------
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=filter(lambda num: num%2==0,numbers)
square=map(lambda num: num**2,even_numbers)
print(list(square))
string=map(lambda num:f"square : (num)",square)








