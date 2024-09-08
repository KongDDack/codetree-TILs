a=int(input())
arr=list(map(int,input().split()))

def absolute_value(n):
    if n<0:
        n=-n
    else:
        n=n
    return n

for elem in arr:
    print(absolute_value(elem),end=" ")