a,o,c=input().split()
a=int(a)
c=int(c)

def plus(a,c):
    return (a+b)
def minus(a,c):
    return (a-b)
def division(a,c):
    return (int(a/c))
def multiple(a,c):
    return (int(a*c))

if o=='+':
    print(f"{a} + {c} = {plus(a,c)}")

elif o=='-':
    print(f"{a} - {c} = {minus(a,c)}")
elif o=='/':
    print(f"{a} / {c} = {division(a,c)}")
elif o=='*':
       print(f"{a} * {c} = {multiple(a,c)}")
else:
    print("False")