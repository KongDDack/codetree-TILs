a=input()
c=list(a)
for i in range(len(c)):
    if c[i]==a[1]:
        c[i]=a[0]
print("".join(c))