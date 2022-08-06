for i in range(int(input())):
    t = input().split()
    n = int(t[0]) # guests 
    a = int(t[1]) # fruits 
    b = int(t[2]) # vegetable 
    c = int(t[3]) # fishes 
    count_c1 = 0
    count_c2 = 0
    p = [a,b,c]
    q = max(p)
    for i in range(q):    
        if a >= 1 and b >= 1:
            count_c1 = count_c1 + 1
            a = a - 1
            b = b - 1  
        if b >= 1 and c >= 1:
            count_c2 = count_c2  + 1
            b = b - 1 
            c = c - 1
    if count_c1 + count_c2 >= n:
        print('YES')
    else:
        print('NO')
    count_c1 = 0
    count_c2 = 0
    
