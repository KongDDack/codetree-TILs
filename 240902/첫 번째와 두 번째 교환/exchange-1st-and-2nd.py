s=input()
arr=list(s)
a=[]


for i in range(len(arr)):
    if arr[i]==arr[0]:
        a.append(arr[1])
    elif arr[i]==arr[1]:
        a.append(arr[0])
    else:
        a.append(arr[i])
print("".join(a))