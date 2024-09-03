a=input()
c=list(a)
while True:
    b=int(input())
    if b<len(c):
        c.pop(b)
        print("".join(c))
        if len(c)==1:
            break
    elif b>=len(c):
        c.pop(-1)
        print("".join(c))
        if len(c)==1:
            break