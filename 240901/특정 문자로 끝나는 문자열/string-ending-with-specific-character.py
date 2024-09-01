arr=[
    input()
    for _ in range(10)
]
arr2=[]
n=input()
for elem in arr:
    if elem[-1]==n:
        arr2.append(elem)
if len(arr2)!=0:
    for elem in arr2:
        print(elem)
else:
    print('None')