names=["Ali","Saba","Sara","Reza"]
for index,name in enumerate(names,start=1):
    print(index,name)
#p2
numbers=[15,2,9,30,7]
new_numbers=sorted(numbers)
print(numbers)
print(new_numbers)
#p3
grades=[18,15,20,8]
print(any(grade == 20 for grade in grades))
#p4
grades=[18,20,17,19]
print(all(grade >= 10 for grade in grades))
#------------------------
#warm up
books=["python","ai","math","english"]
for index,book in enumerate(books,start=1):
    print(f"book{index}:{book}")
#p2 
scores=[18,7,20,15,9,19]
sorted_scores=sorted(scores)
print(sorted_scores)
reverse=sorted(scores,reverse=True)
print(reverse)
#p3
grades=[12,15,18,20,9]
if any(grade==20 for grade in grades):
        print("excelent")
else:
        print("no excelent student") 
#p4
ages=[20,25,18,30]
if all(age> 18 for age in ages):
        print("all are adult")
else:
        print("they are minors")
#boss fight 
with open("note.txt","w") as file:
    file.write("python")
    file.write("\nai")
    file.write("\nmachine learning")
    file.write("\ndata science")
with open("note.txt","r")as file:
    print(file.read())
with open("note.txt","w")as file:
    for index,note in file("note.txt"):
        file.write(f"{index}.{note}")
with open("note.txt","w")as file:
    sorted(file)
with open("note.txt","r")as file:
    print(file.read())
