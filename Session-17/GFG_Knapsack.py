class Solution:
    def knapsack(self, W, val, wt):
        n = len(val)
        dp = [0] * (W + 1)
        
        for i in range(n):
            for w in range(W, wt[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - wt[i]] + val[i])
                
        return dp[W]