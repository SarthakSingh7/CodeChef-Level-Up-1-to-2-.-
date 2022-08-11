for i in range(int(input())):
    t = input().split()
    u = int(t[0])
    v = int(t[1])
    a = int(t[2])
    s = int(t[3])
    if u**2 >= 2*a*s:
        vel = (u**2 - 2*a*s)**(1/2)
        if vel <= v:
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')
