arr=[]
cnt=0
while True:
    n=input()
    if n=='0':
        break
    cnt+=1
    if cnt%2==1:
        arr.append(n)
print(cnt)
for elem in arr:
    print(elem)