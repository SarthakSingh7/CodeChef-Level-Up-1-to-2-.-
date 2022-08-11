for i in range(int(input())):
    t = input().split()
    n = int(t[0])
    k = int(t[1])
    div = int(n/k)
    if k == 0:
       print(n)
    elif n >= k:
        print(n%k)
    else:
        print(n)
