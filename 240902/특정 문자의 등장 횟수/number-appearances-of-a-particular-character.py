a=input()
cnt=0
cnnt=0
for i in range(len(a)-1):
    if a[i]=='e' and a[i+1]=='e':
        cnt+=1
    if a[i]=='e' and a[i+1]=='b':
        cnnt+=1
print(cnt,cnnt)