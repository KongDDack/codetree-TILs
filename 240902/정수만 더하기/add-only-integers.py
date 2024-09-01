a=input()
b=[]
for elem in a:
    if elem.isdigit():
        b.append(int(elem))
print(sum(b))