a,b=map(int,input().split())
def plus_multiple(a,b):
    if a>b:
        a=a+25
        b=b*2
        return a,b
    elif b>a:
        b=b+25
        a=a*2
        return a,b

print(*plus_multiple(a,b))