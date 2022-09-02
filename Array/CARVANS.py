for i in range(int(input())):
    n = int(input())  # num of cars
    t = input().split()  # max spped of the cars
    count = 0  
    count1 = []
    if n == 1:
        count = 1
    elif n>1:
        mx = int(t[0])
        for i in range(len(t)):
            if int(t[i]) <= mx:
                mx  = int(t[i])
                count = count + 1
                count1.append(t[i])
                #print(mx)
    print(count)  
