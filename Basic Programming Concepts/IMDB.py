for i in range(int(input())):
    nx = input().split()
    n = int(nx[0])
    x = int(nx[1])   # storage available 
    lis = []
    for i in range(n):
        tc = input().split()
        s = int(tc[0])  # space req
        r = int(tc[1])  # rating 
        lis.append(s)
        lis.append(r)
    lis2 = []    
    for i in range(len(lis)):
        max_r = 0
        if i%2 == 0 and lis[i] <= x and lis[i+1] >= max_r:
            max_r = lis[i+1]
            lis2.append(max_r)
    print(max(lis2))  
    lis2 = []
