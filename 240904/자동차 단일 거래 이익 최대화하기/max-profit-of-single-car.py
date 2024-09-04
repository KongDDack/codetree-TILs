n=int(input())
arr=list(map(int,input().split()))
profits=[]
lastprofits=[]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        profits.append(arr[j]-arr[i])
    
    lastprofits.append(max(profits))
print(max(lastprofits))