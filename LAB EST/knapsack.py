def knapsack(W, val, wt):
    n = len(val)
    dp = [0] * (W + 1)
    
    for i in range(n):
        for w in range(W, wt[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - wt[i]] + val[i])
            
    return dp[W]

W = 4
val = [1, 2, 3]
wt = [4, 5, 1]

print(knapsack(W, val, wt))