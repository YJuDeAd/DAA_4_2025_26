class Solution:
	def perfectSum(self, arr, target):
		dp = [0] * (target + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[target]