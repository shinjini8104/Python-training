dict={'A':1,'B':10,'C':100,'D':1000,'E':10000,'F':100000}
ip="ABCFDAABCCC"
res=1
for i in ip:
    if(i in dict):
        res=res+dict[i]
print(res)