M,D=map(int,input().split())

def date_judge(n):
    if n<=31:
        return True
    else:
        return False
def date_judge2(n):
    if n<=30:
        return True
    else:
        return False
def date_judge3(n):
    if n<=28:
        return True
    else:
        return False
if M==2:
    if date_judge3(D):
        print("Yes")
    else: 
        print("No")
elif M==1 or 3 or 5 or 7 or 8 or 10 or 12:
    if date_judge(D):
        print("Yes")
    else: 
        print("No")

elif M== 2 or 4 or 6 or 9 or 11:
    if date_judge2(D):
        print("Yes")
    else: 
        print("No")