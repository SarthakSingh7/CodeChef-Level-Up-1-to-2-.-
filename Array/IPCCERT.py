l1 = input().split()
n = int(l1[0])   # n stu participating 1 to n
m = int(l1[1])   # must watch atleast m min 
k = int(l1[2])   # num of lec 
qual = 0
for i in range(n):
    t = input().split()     # t1 ... tk, Q questions
    q = int(t[-1])
    t.remove(t[-1])
    c = 0 # count of min
      # qualified count
    for i in t:
        c = c + int(i)
    if q <= 10 and c >= m:
        qual = qual + 1
        c = 0    
print(qual)        
