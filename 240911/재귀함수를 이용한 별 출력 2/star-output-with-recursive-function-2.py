n=int(input())
def function1(n):
    if n==0:
        return
    print("* "*n)
    function1(n-1)
    

def function2(n):
    if n==0:
        return
    function2(n-1)
    print("* "*n)


function1(n)
function2(n)