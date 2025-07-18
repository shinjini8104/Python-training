def rcb ():
    return len([[2,3],[5,6,7]])

def csk():
    raj=[3,4,5]
    return raj[1]
def mi(a):
    return len(str(a))

def GT(s):
    d=list(s)
    return len([i for i in d if i in "aeiou"])
a=GT("Gill")
for i in  range(rcb()):
    a=a+csk()
print(a*mi(3))

for num in range(100, 1000):
    if is_prime(num):
        digits = [int(d) for d in str(num)]
        if all(is_prime(d) for d in digits):
            if is_prime(sum(digits)):
                print(num)
  