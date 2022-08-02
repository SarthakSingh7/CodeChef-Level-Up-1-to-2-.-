for i in range(int(input())):
    sp = input().split()
    hp_max = 0
    A = int(sp[0])
    B = int(sp[1])
    C = int(sp[2])
    li = [A,B,C]
    hp_max = hp_max + max(li)
    li.remove(max(li))
    hp_max = hp_max + max(li)
    print(hp_max)
