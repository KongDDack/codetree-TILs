def function(a1,a2):
    sum_val=0
    for i in range(a1,a2+1):
        sum_val+=arr[i-1]
    print(sum_val)

n,m=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(m):
    a1,a2=map(int,input().split())
    function(a1,a2)