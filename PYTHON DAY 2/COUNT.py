s=input(" Enter a sentence ")
c=0
for i in range (len(s)):
    if(s[i]==" " and s[i+1]!=" "):
        c=c+1
print("The number of words are",c)
