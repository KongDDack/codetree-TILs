a,b=input().split()
c=ord(a)
d=ord(b)
if c>=d:
    e=c-d
else:
    e=d-c
print(c+d,e)