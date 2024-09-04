s,q=input().split()


q=int(q)
for i in range(q):
    quest=input().split()
    if int(quest[0])==1:
        a=int(quest[1])
        b=int(quest[2])
        tmp=s[a-1]
        s=s[:a-1]+s[b-1]+s[a:]
        s=s[:b-1]+tmp+s[b:]
        print(s)
    else:
        a=quest[1]
        b=quest[2]
        for i in range(len(s)):
            if s[i]==a:
                s=s[:i]+b+s[i+1:]
        print(s)