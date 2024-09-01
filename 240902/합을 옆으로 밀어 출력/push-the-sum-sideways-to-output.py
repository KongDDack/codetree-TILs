n=int(input())
sum_val=0
for i in range(n):
    a=int(input())
    sum_val+=a
print(str(sum_val)[1:]+str(sum_val)[0])