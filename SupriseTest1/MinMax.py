def maxMin(k, arr):
    arr.sort()
    
    n = len(arr)
    min_u = float('inf')
    
    for i in range(n - k + 1):
        unf = arr[i + k - 1] - arr[i]
        min_u = min(min_u, unf)
        
    return min_u