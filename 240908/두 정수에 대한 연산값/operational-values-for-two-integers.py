a,b=map(int,input().split())
def plus_multiple(a,b):
    if a>b:
        a=a+25
        b=b*2
        
    elif b>a:
        b=b+25
        a=a*2
    return a,b    

a,b=plus_multiple(a,b)
print(a,b)