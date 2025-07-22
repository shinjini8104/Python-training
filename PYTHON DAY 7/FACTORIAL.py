def fact():
    if(n<=1):
        return 1
    else:
        return n* fact(n-1)
n=int(input("entrer any number"))
fact(n)