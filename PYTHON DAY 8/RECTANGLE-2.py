import random
class rect:
    def set_dim(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b

nums=[]
d=int(input("Enter no of rectangle:"))
for i in range(d):
    R=rect()
    R = rect(random.randint(1, 5), random.randint(5, 13))
    nums.append(R)
    a=int(input("Enter length of rectangle:"))  
    b=int(input("Enter breadth of rectangle:"))  
    R.set_dim(a,b)
    nums.append(R)

iii=1
for i in nums:
    print("area of Rect {} : is {}".format(iii,i.area()))
    iii = iii+1
for i in nums:
    if i.area() % 2 == 0:
        print(i.area())
for i in nums:
    print(" i.a")