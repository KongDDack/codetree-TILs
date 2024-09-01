n=input()
arr=['apple','banana','grape','blueberry','orange']
arr2=[]
for i in range(5):
    if arr[i][2]==n or arr[i][3]==n:
        arr2.append(arr[i])
for elem in arr2:
    print(elem)
print(len(arr2))