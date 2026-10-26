#list_methods
numbers=[1,2,3]
numbers.extend([4,5,6])
print(numbers)
#p2
names=["ali","saba","roya","saba"]
print(names.count("saba"))
#p3
numbers=[15,3,20,7,9]
numbers.sort()
numbers.reverse()
print(numbers)
#p4
cities=["tehran","arak","tabriz"]
print(numbers[1])
print(cities.index("arak"))
#boss fight
numbers=[5,8,2]
new_numbers=numbers.copy()
new_numbers.extend([10,20])
new_numbers.sort()
print(new_numbers)
#-----------------------------------------------------
#nightmare challenge
grades=[18,20,7,15,18,9]
new_grades=grades.copy()
new_grades.extend([16,19])
new_grades.reverse()
max_grade=max(new_grades)
min_grade=min(new_grades)
average=sum(new_grades)/len(new_grades)
print(new_grades.count(18))
print(new_grades.index(20))
gradeA=[grade for grade in new_grades if grade>18]
grade_A=map(lambda grade: f"Grade : {grade}",new_grades)
print(list(grade_A))
bigger_17=filter(lambda grade: grade > 17,new_grades)
print(list(bigger_17))
print("-"*30)
print(f"Total students: {bigger_17}")
print(f"Average : {average}")
print(f"Highest : {max_grade}")
print(f"lowest : {min_grade}")
print(f"passed students : {grade_A}")
print(f"Excelent student : {gradeA}")





