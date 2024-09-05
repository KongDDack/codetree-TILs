def common_diviser(n,m):
    cnt=0
    if n>=m:
        for i in range(1,m+1):
            if n%i==0 and m%i==0:
                cnt=i
    else:
        for i in range(1,n+1):
            if n%i==0 and m%i==0:
                cnt=i
    print(cnt)

a,b=map(int,input().split())
common_diviser(a,b)