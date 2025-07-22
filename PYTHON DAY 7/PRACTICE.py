def hello(n):
    return n+2
def hai(n):
    a=hello(n-1)
    if(n==2):
        return
    b=hello(n-2)
    print("hai")
    print(a)

print(hai(5))