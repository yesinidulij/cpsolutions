def solve(n,m,k,arr):
    if m < k:
        return 'NO'
    
    arr.sort()
    curr_mex = 0
    count = 0
    
    for i in range(n):
        if arr[i] == k:
            continue
        
        if arr[i] > k:
            break
        
        if arr[i] == curr_mex:
            curr_mex += 1
        
        count += 1
        
    if curr_mex != k:
        return 'NO'

    if count >= m:
        return 'YES'
    
    for i in range(n-1,-1,-1):
        if arr[i] > k:
            count += 1
        else:
            break
    
    if count >= m:
        return 'YES'
    
    return 'NO'
    
for _ in range(int(input())):
    n,m,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(solve(n,m,k,arr))