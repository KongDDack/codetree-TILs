arr=[
    [0 for _ in range(3)]
    for _ in range(3)
]
arr2=[
     [0 for _ in range(3)]
    for _ in range(3)
]
arr3=[
     [0 for _ in range(3)]
    for _ in range(3)
]
num=1
for i in range(3):
    for j in range(3):
        arr[i][j]=num
        num+=1

num=2
for i in range(3):
    for j in range(3):
        arr2[i][j]=num
        num+=1

for i in range(3):
    for j in range(3):
        arr3[i][j]=arr[i][j]*arr2[i][j]

for row in arr3:
    for elem in row:
        print(elem,end=" ")
    print()