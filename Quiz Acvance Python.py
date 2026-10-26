#mixed project
students={
    "Ali":18,
    "saba":20,
    "sara":9,
    "reza":15,
    "roya":19
}
passed=[value for value in students.values() if value>= 10]
print(passed)
passedp2=list(map(lambda value: value+2, passed))
print(list(passedp2))
average=sum(passedp2)/len(passed)
with open("report2.txt","w")as file:
    file.write(f"Passed grades: {passedp2}")
    file.write(f"\nAverage: {average}")
#p2
products={
    "milk":80,
    "bread":40,
    "egg":120,
    "rice":250,
    "tea":180
}
bigger100=[value for value in products.values() if value>100]
offer=list(map(lambda value: value* 0/9,bigger100))
with open("discount.txt","w")as file:
    for price in offer:
        file.write(f"{price}\n")
#p 3
students={
    "Ali":18,
    "sara":9,
    "reza":14,
    "saba":20,
    "nima":7
}
passed=[a for a in students.values() if a>=10]
plus1=list(map(lambda x: x+1 if x<20 else x,passed))
average=sum(plus1)/len(plus1)
with open("result.txt", "w")as f:
    f.write(f"Passed grades: {plus1}")
    f.write(f"Average : {average}")
#p4
employees = {
    "Ali": 18000000,
    "Saba": 25000000,
    "Sara": 9000000,
    "Reza": 15000000,
    "Roya": 30000000
}
biggerlist=[value for value in employees.values()]
bigger15M=list(filter(lambda value: value>=15000000,biggerlist))
result=list(map(lambda value: value+value*15/100,bigger15M ))
bigger20M=[value for value in result if value>=20000000]
average=sum(bigger20M)/len(bigger20M)
with open("salary_report.txt","w")as f:
    for x in bigger20M:
        f.write(f"\n{x}")
    f.write(f"\nAve:{average}")
    f.write(f"\n{result}")
    f.write(f"\n{bigger15M}")
#p Qwen
#بسم الله 
raw_tempetures=[72,None,85,-500,90,68,None,77,105,-10,30,110]
# Level 1
tempetures=list(filter(lambda temp: temp is not None and temp>=0 ,raw_tempetures))
#level 2 
santyGrad=list(map(lambda x: (x-32)*5/9,tempetures))
#level 3
rounded_data=list(map(lambda z: round(z,1) ,santyGrad))
#level 4
hot_day=list(filter(lambda c: c>=25,rounded_data))
#boss fight 
santyGrad2=list(map(lambda y: round((y-32)*5/9,1) ,tempetures))

# list comprehension
even_numbers=[num for num in range(0,20,2)]
print(even_numbers)