students={
    "Ali":18,
    "Saba":20,
    "Sara":9,
    "Reza":15,
    "Roya":19
}
for key,value in students.item():
    print(f"average : {sum(value)/len(value)}")
print(max(value))
print(min(value))
passed= filter(lambda value: value>=10,students)
print(len(passed))
excelent=filter(lambda value: value >= 18,students)
print(list(excelent))