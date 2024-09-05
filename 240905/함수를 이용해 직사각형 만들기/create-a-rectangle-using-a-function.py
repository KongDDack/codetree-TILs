def rectangle(n,m):
    for i in range(n):
        print("1"*m)

row,column=map(int,input().split())

rectangle(row,column)