a,b=map(int,input().split())
def prime_number(n):
    for i in range(2,n):
        if n%i==0:
            return False

    return True

cnt=0
for i in range(a,b+1):
    if prime_number(i):
        cnt+=i
    if a==1:
        cnt-=1
print(cnt)