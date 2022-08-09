for i in range(int(input())):
    t = input().split()
    n = int(t[0])
    s = int(t[1])  # sum of tastiness 
    out = 0
    if n >= s:
        out = s
    elif n<s:
        out = abs(n - (s - n))
    print(out)    
    out = 0
