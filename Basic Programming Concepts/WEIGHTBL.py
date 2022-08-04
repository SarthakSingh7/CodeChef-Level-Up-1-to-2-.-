for i in range(int(input())):
    tc = input().split()
    w1= int(tc[0])
    w2= int(tc[1])
    x1= int(tc[2])
    x2= int(tc[3])
    m= int(tc[4])
    
    c1 = w1 + m*x1  # min value from case 1 
    c2 = w1 + m*x2  # max value of wt using case x
    # the value of wt should be in range of c1 and c2 
    if c1 <= w2 <= c2:
        print(1)
    else:
        print(0)
    
    
