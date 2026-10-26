#List Ccomprehension
#p1
numbers=[2,4,6,8]
new_numbers=[num*3 for num in numbers]
print(new_numbers) 
#p2
names=["ali","saba","roya"]
title_names=[name.title() for name in names]
print(title_names)
#p3
numbers=[1,2,3,4,5,6]
even_numbers=[num for num in numbers if num%2==0]
print(even_numbers)
#p4
prices=[100,200,300]
new_prices=[price+50 for price in prices]
print(new_prices)
#boss fight 
numbers=[1,2,3,4,5]
new_numbers=[num**2 if num%2==0 else num**3 for num in numbers]
print(new_numbers)
#QWEN
#questin 7
square=[num**2 for num in range(1,11)]
print(super)
#q8
mutiple_3=[num for num in range(1,31) if num%3==0]
print(mutiple_3)
#q9
words=["hello","python","world"]
print(words.upper())
#sadly i dont know
numbers=[num**2 for num in range(1,21) if num%2==0]
print(numbers)


