n=input()
arr=['apple','banana','grape','blueberry','orange']
arr2=[]
for i in range(5):
    if arr[i][2]==n or arr[i][3]==n:
        arr2.append(arr[i])
print(arr2[0])
print(arr2[1])
print(arr2[2])
print(len(arr2))