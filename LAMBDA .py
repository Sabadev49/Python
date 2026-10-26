# p 1
numbers=[1,2,3,4,5]
new_numbers=map(lambda num:num*5 , numbers)
print(list(new_numbers))
# p 2
names=["ali","saba","roya"]
title_names=map(lambda name: name.title(),names)
print(list(title_names))
#p3 
prices=[100,250,400]
new_price=map(lambda price: price+20, prices)
print(list(new_price))
# --------------------------------------------------
numbers=[5,8,10,20]
new_numbers=map(lambda num: num**2, numbers)
print(list(new_numbers))
#p2
words=["python","Java","c++","html"]
new_words=map(lambda word: word.upper(), words)
print(list(new_words))
#p3
grades=[12,15,18,20]
new_grades=map(lambda grade: grade+2,grades)
print(list(new_grades))
#p4
cities=["tehran","arak","tabriz","shiraz"]
f_cities=map(lambda city:f"city: {city}",cities)
print(list(f_cities))
#p5
numbers=[2,4,6,8]
new_numbers=map(lambda num:f" number : {num}",numbers)
print(list(new_numbers))
#p6
prices=[100000,250000,800000,600000]
takhfif=map(lambda price: price-(price/10) if price>500000 else price , prices)
print(list(takhfif))
#p7 
ages=[8,15,20,70,30]
status=map(lambda age:"senior" if age >= 70 else "Adult" if age>=18 else "child") 
#boss fight
names=["ali","saba","roya","sam"]
greeting=map(lambda name: f"Hello {name} ❤",names)
print(list(greeting))
#super boss
numbers=[1,2,3,4,5]
evenorodd=map(lambda num: "Even" if num%2==0 else "odd")
print(list(evenorodd))