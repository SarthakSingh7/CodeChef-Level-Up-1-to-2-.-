for i in range(int(input())):
    n,k = map(int,input().split())
    arr = map(int,input().split())
    s_arr = sum(arr) # sum of the elements of the array
    print(s_arr%k)
# the sum of the digits will also be divisble by k
# the modulys operator on the sum
# sum%k gives us the remainder 
    
    
    
