N=int(input())
def number(n):
    if n==0:
        return 0
    print(n, end=" ")
    number(n-1)
    print(n, end=" ")

number(N)