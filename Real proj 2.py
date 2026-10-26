#real proj 2
students={
    "ali":18,
    "saba":20,
    "sara":9,
    "reza":15,
    "roya":19
}
avarage=sum(students.values())/len(students.values())
print(avarage)
passed=0
for key,value in students.items():
    if value >= 10:
        print(key)
        passed+=1
excelent=[]
ex=0
for key,value in students.items():
    if value >= 18:
        excelent.append(key)
        print(excelent)
        ex+=1
#excelent=[value for value in students.values() if value >= 18 ]
with open("report.txt","w")as file:
    file.write(f"Average:{avarage}\n")
    file.write(f"passed:{passed}\n")
    file.write(f"excelent:{ex}\n")
with open("report.txt","r")as file:
    print(file.read())
highest=0
#---------------------------
mutiple5=lambda num: "Yes" if num%5==0 else "no" 
print(mutiple5(4))
#p2
lower_num=lambda num1,num2,num3: num1 if num1>num2 and num1>num3 else num2 if num2>num1 and num2>num3 else num3
print(lower_num(1287,1288,2945))
#p3
prices=[100,250,400,600]
new_prices=map(lambda price: price + 50,prices)
print(list(new_prices))
#p4
words=["python","c","java","go","javascript"]
longers=filter(lambda word: len(word)>4,words)
print(list(longers))
# boss fight
numbers=[2,5,8,11,14,17,20]
even=filter(lambda num: num%2==0,numbers)
square=map(lambda num: num**2,even)
print(list(square)) 

        
