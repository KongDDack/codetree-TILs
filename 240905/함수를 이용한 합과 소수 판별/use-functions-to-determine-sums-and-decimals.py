a,b=map(int,input().split())
def thatnumber(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def thatnumber2(n):
    n=str(n)
    sum_val=0
    for i in range(len(n)):
        sum_val+=int(n[i])
    if sum_val%2==0:
        return True
    else:
        return False
    
cnt=0
for i in range(a,b+1):
        if thatnumber(i) and thatnumber2(i):
            cnt+=1
    
print(cnt)