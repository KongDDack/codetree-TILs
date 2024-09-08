a=input()
b=input()

def include(a,b):
    if b in a:
        print(a.find(b))
    else:
        print(-1)

include(a,b)