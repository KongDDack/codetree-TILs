sum_val=0

arr2=[
    list(map(int,input().split()))
    for i in range(2)
]
for i in range(2):
    aver=sum(arr2[i])/4
    print(f"{aver:.1f}",end=" ")
print()

for i in range(4):
    sum3=0
    for j in range(2):
        sum3+=arr2[j][i]
        aver2=sum3/2
    print(f"{aver2:.1f}",end=" ")
print()

for i in range(2):
    sum_val+=sum(arr2[i])
print(f"{sum_val/8:.1f}",end=" ")