for i in range(int(input())):
    n = int(input())
    t = input().split()
    oil = int(t[0])
    dis = 0
    for i in range(1,n):
        if oil == 0:
            break
        oil = oil + int(t[i]) - 1
        dis = dis + 1
    if oil != 0:
        dis = dis + oil 
    print(dis)
        
