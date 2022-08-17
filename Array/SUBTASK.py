for i in range(int(input())):
    t = input().split() # N M K 
    a = input().split()
    n = int(t[0])
    m = int(t[1])
    k = int(t[2])
    count = 0
    for i in a:
        if i == '1':
            count = count + 1
        elif i == '0':
            break
    if count == n:
        print(100)
    elif count >= m and count < n:
        print(k)
    elif count != n and count != m:
        print(0)
        

    
