n,m=map(int,input().split())
arr1=[]
arr2=[]
for i in range(n):
    arr=list(map(int,input().split()))
    arr1.append(arr)
for i in range(n):
    arr=list(map(int,input().split()))
    arr2.append(arr)

arr3=[
    [0 for _ in range(m)]
    for _ in range(n)
]
for i in range(n):
    for j in range(n):
        if arr1[i][j]==arr2[i][j]:
            arr3[i][j]=0
        else:
            arr3[i][j]=1
for row in arr3:
    for elem in row:
        print(elem,end=" ")
    print()