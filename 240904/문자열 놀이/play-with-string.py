s,q=input().split()
p=list(s)
q=int(q)
for _ in range(q):
    c,a,b=input().split()
    arr=[c,a,b]
    if arr[0]=='1':
        p[int(a)-1]=s[int(b)-1]
        p[int(b)-1]=s[int(a)-1]
        print("".join(p))
    elif arr[0]=='2':
        for i in range(len(p)):
            if p[i]==a:
                p[i]=b
                
        print("".join(p))