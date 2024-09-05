y=int(input())
def is_leapyear(y):
    if y%4!=0:
        return False
    if y%100==0 and y%400!=0:
        return False
    return True

if is_leapyear(y):
    print('true')
else:
    print('false')