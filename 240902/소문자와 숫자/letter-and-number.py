a=input()
c=[]
for elem in a:
    if elem.isalpha():
        c.append(elem)
    elif elem.isdigit():
        c.append(elem)
d="".join(c)
print(d.lower())