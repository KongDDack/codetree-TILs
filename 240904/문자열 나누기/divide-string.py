n=int(input())
arr=input().split()

tot_str="".join(arr)

s=""
for i in range(len(tot_str)):
    print(tot_str[i],end="")
    if (i+1)%5==0:
        print()