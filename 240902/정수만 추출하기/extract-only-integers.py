a,b=input().split()
c=[]
d=[]
for elem in a:
    if elem.isdigit():
        c.append(elem)
    else:
        break
for elem in b:
    if elem.isdigit():
        d.append(elem)
    else:
        break
e="".join(c)
f="".join(d)

print(int(e)+int(f))