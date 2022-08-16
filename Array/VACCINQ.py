for i in range(int(input())):
    t = input().split()
    n = int(t[0])  # n people 
    p = int(t[1])  # chef position p th
    x = int(t[2])  # time for child 
    y = int(t[3])  # time for adult 
    # 0 child, 1 = adult 
    a = input().split() # array 
    temp = a[0:p]  #small arrray icluding the chef 
    c1 = temp.count('1')
    c2 = temp.count('0')
    
    total_time = c1 * y + c2 * x
    print(total_time)
