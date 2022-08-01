for i in range(int(input())):
    tc = input().split()
    D = int(tc[0])  # first dose D days ago
    L = int(tc[1])  # second dose min time 
    R = int(tc[2])  # second dose max time 
    if D < L:
        print('Too Early')
    elif D>=L and D>R:
        print('Too Late')
    elif D>=L and D<=R:
        print('Take second dose now')
    
