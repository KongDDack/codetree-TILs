n=int(input())
arr=[
    input()
    for _ in range(n)
]
sum_val=0
a_val=0
for elem in arr:
    sum_val+=len(elem)
    if elem[0]=='a':
        a_val+=1
print(sum_val,a_val)