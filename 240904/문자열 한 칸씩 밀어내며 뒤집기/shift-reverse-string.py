a,q=input().split()
q=int(q)

for i in range(q):
    b=int(input())
    if b==1:
        a=a[1:]+a[0]
        print(a)
    elif b==2:
        a=a[-1]+a[0:-1]
        print(a)
    elif b==3:
        a=a[::-1]
        print(a)