a=input()
c=[]
for i in range(len(a)):
    if i%2==1:
        c.append(a[i])
print("".join(c)[::-1])