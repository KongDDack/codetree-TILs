N=int(input())

def function(n):
    if n==1:
        return 1
    return function(n-1)+n

print(function(N))