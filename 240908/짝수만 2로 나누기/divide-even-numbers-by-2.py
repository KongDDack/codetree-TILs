n=int(input())
arr=list(map(int,input().split()))
def even_number(n):
    if n%2==0:
        return int(n/2)
    else:
        return n 

for elem in arr:
    print(even_number(elem),end=" ")