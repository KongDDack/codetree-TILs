N=int(input())
def number(n):
    if n==0:
        return
    number(n-1)
    print(n, end=" ")

def backnumber(n):
    if n==0:
        return
    print(n,end=" ")
    backnumber(n-1)

number(N)
print()
backnumber(N)