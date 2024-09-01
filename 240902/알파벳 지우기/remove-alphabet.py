a=input()
b=input()
c=[]
d=[]
for elem in a:
    if elem.isdigit():
        c.append(elem)
for elem in b:
    if elem.isdigit():
        d.append(elem)
print(int("".join(c))+int("".join(d)))