for i in range(int(input())):
    t = 0
    tc = input().split()   # A B X
    A = int(tc[0])
    B = int(tc[1])
    X = int(tc[2])
    while int(t) < ((B - A)/X):
        t = t + 1
    print(t)    
