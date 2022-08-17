for i in range(int(input())):
    n = int(input())
    t = input().split()
    lis = []
    req = ['1','2','3','4','5','6','7']
    count_req = 0
    count = 0
    for i in t:
        if i in req:
            lis.append(i)
            req.remove(i)
            count_req = count_req + 1
            if count_req == 7:
                break
        elif count_req != 7 :
            count = count + 1
    print(count_req + count)        
            
            
            
