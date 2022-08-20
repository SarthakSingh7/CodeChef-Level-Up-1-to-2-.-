for i in range(int(input())):
    t = input().split()
    m = int(t[0])   # number of houses
    x = int(t[1])   # max speed of x houses per min
    y = int(t[2])   # will search for y minutes
    tc = input().split()
    max_h = x*y   # max houses search in y min 
    r = []
    l = []
    lis =[]
    for i in tc:
        a = int(i) + max_h
        b = int(i) - max_h
        if a <= 100:
            r.append(a) 
        elif a > 100:
            r.append(100)
        if b <= 0:
            l.append(1)
        elif b > 0:
            l.append(b)
    for i in range(m):
        x = [j for j in range(l[i],r[i]+1)]
        for j in x:
            lis.append(j)
            x = []
    count = 0        
    for i in range(1,101):
        if i not in set(lis):
            count = count + 1
    print(count)
