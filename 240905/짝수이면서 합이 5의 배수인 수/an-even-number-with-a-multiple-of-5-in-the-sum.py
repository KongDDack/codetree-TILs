n=int(input())

def is_magicnumber(a):
    if a%2==0 and (a//10+a%10)%5==0:
        return 'Yes'
    else:
        return 'False'

print(is_magicnumber(n))