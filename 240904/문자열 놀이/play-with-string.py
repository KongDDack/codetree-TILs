s,q=input().split()
k=list(s)

q=int(q)
for i in range(q):
    quest=input().split()
    if quest[0]=='1':
        a=int(quest[1])
        b=int(quest[2])
        k[a-1]=s[b-1]
        k[b-1]=s[a-1]
        print("".join(k))
    else:
        for i in range(len(k)):
            if k[i]==quest[1]:
                k[i]=quest[2]
        print("".join(k))