num=int(input("Enter any num:"))

def cop(a,b):
    return gcd(a,b)==1
def gcd(a,b):
    while(b!=0):
        temp=a
        a=b
        b=temp % b
    return a
    

for i in range(1,num):
    for j in range(1,i):
        for k in range(1,j):
            if(j*j + k*k== i*i and cop(i,j) and cop(i,k) and cop(i,k)):
                print(k,j,i)