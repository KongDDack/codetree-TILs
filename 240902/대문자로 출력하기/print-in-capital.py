n=input()
a=[]
for elem in n:
    if elem.isalpha():
        a.append(elem)

c="".join(a)
print(c.upper())