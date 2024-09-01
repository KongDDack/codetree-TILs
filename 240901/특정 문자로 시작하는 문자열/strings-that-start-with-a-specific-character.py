n=int(input())
arr=[
    input()
    for _ in range(n)
]
s=input()
cnt=0
sum_val=0
for elem in arr:
    if elem[0]==s:
        cnt+=1
        sum_val+=len(elem)
print(cnt,f"{sum_val/cnt:.2f}")