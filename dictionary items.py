book_information={
    "title" : "life" ,
    "author": "saba",
    "price": 140000 
    }
print(book_information.keys())
#project 2
book_information={
    "title" : "life" ,
    "author": "saba",
    "price": 140000 
    }
print(book_information.values())
#project 3
book_information={
    "title" : "life" ,
    "author": "saba",
    "price": 140000 
    }
for items in book_information:
    print(book_information.items())
#project 4
book_information={
    "title" : "life" ,
    "author": "saba",
    "price": 140000 
    }
print(book_information.get("price"))
print(book_information.get("pulisher", "not found"))
#boss fight
studen_grades={
    "saba":16,
    "setayesh":17.5 ,
    "rahman":19,
    "nasim": 20,
    "parimah": 2

}
for name , grade in studen_grades.items() :
    if grade() > 17:
        print(name,grade)