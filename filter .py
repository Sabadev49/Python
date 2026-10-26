#p 1
numbers=[1,2,3,4,5,6,7,8]
even_numbers=filter(lambda num: num%2==0,numbers)
print(list(even_numbers))
#p2
names=["ali","saba","sam","raya","sina"]
new_name=filter(lambda name: name.startswith("s"), names)
print(list(new_name))
#p3
prices=[100000,700000,50000,90000]
new_price=filter(lambda price: price > 500000,prices)
print(list(new_price))
#p4
words=["python","Java","c","javascript","go"]
filterd_words=filter(lambda word: len(word) > 4 ,words)
print(list(filterd_words))
#boss fight
ages=[10,17,18,22,60,15]
adult=filter(lambda age: age>=18 ,ages)
print(list(adult))
