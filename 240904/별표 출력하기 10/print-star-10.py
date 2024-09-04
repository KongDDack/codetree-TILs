n=int(input())
for i in range(2*n):
    if i%2==0:
        for _ in range(1+int(i//2)):
            print("*",end=" ")
    else:
        for _ in range(n-int((i-1)/2)):
            print("*",end=" ")
    print()