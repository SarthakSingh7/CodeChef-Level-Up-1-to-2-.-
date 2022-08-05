for i in range(int(input())):
    tc = input().split()
    s = int(tc[0])  # share price 
    a = int(tc[1])  # lower limit
    b = int(tc[2])  # upper limit 
    c = int(tc[3])  # price change by c percent 
    price = s + s * c * (0.01) # share price after change 
    if price >= a and price <= b:
        print('Yes')
    else:
        print('No')
    
