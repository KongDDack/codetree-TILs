a=input()
cnt=1
cur=a[0]
pre=a[0]
result=""
for i in range(1,len(a)):
    cur=a[i]
    if cur==pre:
        cnt+=1
    else:
        result+=pre
        result+=str(cnt)
        cnt=1
        pre=cur
result+=pre
result+=str(cnt)
print(len(result))
print(result)