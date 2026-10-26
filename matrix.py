#p3
matrix=[
    [2,3,4],
    [5,6,7],
    [8,9,10]
]
print(matrix[1][1])
row_3=[row[2] for row in matrix]
print(row_3)
#p4
matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print(matrix[1])
for row in matrix:
    print(row[0])
total=0
for x in matrix:
    total+=sum(x)
print(total)
#p5
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in range(3):
    print(matrix[i][i])
