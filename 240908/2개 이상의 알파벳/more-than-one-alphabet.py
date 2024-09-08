a=input()

def judge(n):
    for i in (len(n)):
        cnt=0
        for j in (len(n)):
            if a[i]!=a[j]:
                cnt+=1
            if cnt>=2:
                return True
                break
    return False

if judge(a):
    print('Yes')
else:
    print('No')