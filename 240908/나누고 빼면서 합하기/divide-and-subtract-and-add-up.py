n,m=map(int,input().split())
arr=list(map(int,input().split()))

def function(m):
    a=arr[m-1]
    while m>1:
        if m%2==0:
            m=m//2
        else:
            m-=1
        a+=arr[m-1]
    return a 

print(function(m))