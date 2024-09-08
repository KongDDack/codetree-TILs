Y,M,D=map(int,input().split())

def season_judge(n):
    if 3<=n<=5:
        return "Spring"
    elif 6<=n<=8:
        return "Summer"
    elif 9<=n<=11:
        return "Fall"
    else:
        return "Winter"

def is_year(n):
    if n%4!=0:
        return False
    
    elif (n%4==0 and n%100==0) and not (n%400==0):
        return False
    return True


def is_date(m,d):
    if is_year(Y):
        if m in [1,3,5,7,8,10,12]:
            if d>31:
                return False
        elif m in [4,6,9,11]:
            if d>30:
                return False
        elif m == 2:
            if d>29:
                return False
        return True
    else:
        if m in [1,3,5,7,8,10,12]:
            if d>31:
                return False
        elif m in [4,6,9,11]:
            if d>30:
                return False
        elif m == 2:
            if d>28:
                return False
        return True

if is_date(M,D):
    print(season_judge(M))
else:
    print(-1)