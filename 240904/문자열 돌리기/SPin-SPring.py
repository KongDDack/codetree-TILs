a=input()
print(a)
for i in range(len(a)):
    print(a[-1]+a[0:-1])
    a=a[-1]+a[0:-1]