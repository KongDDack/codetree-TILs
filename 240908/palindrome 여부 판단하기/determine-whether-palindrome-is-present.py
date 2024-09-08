s=input()
def is_palindrome(a):
    a=a[::-1]
    return a

c=is_palindrome(s)

if s==c:
    print("Yes")
else:
    print("No")