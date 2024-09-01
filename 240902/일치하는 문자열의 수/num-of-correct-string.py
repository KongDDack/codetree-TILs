arr=input().split()
cnt=0
for i in range(int(arr[0])):
    a=input()
    if a==arr[1]:
        cnt+=1
print(cnt)