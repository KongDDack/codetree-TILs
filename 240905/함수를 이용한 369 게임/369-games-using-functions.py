a,b=map(int,input().split())

def threesixnine(n):
    n=str(n)
    for i in range(len(n)):
        if n[i]==3 or n[i]==6 or n[i]==9:
            return True
        


def counting(n):
    return n%3==0 or threesixnine(n)

    
cnt=0
for i in range(a,b+a):
    if counting(i):
        cnt+=1