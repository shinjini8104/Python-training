def cal(x,a,b):
    if a>=x:
        return 1
    time=0
    height=0
    while height + a < x:
        height += (a - b)
        time += 2
    print(time + 1)





cal(30,10,5)
cal(25,7,4)
  
