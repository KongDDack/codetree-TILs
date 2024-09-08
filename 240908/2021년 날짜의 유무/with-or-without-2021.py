M,D=map(int,input().split())

def day_exist(a,b):
    if a in [1,3,5,7,8,10,12]:
        if b>31:
            return False
    elif a in [4,6,9,11]:
        if b>30:
            return False
    elif a ==2:
        if b>28:
            return False
    elif a>12:
        return False
    return True

if day_exist(M,D):
    print("Yes")
else:
    print("No")