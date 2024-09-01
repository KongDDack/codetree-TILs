a=input()
b=[]
for elem in a:
    if elem.isupper():
        b.append(elem.lower())
    else:
        b.append(elem.upper())
print("".join(b))