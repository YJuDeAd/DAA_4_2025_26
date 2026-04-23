class Solution:
	def minDifference(self, arr):
		S = sum(arr)
        target = S // 2
        n = len(arr)
    
        
        dp = [False] * (target + 1)
        dp[0] = True
    
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
    
        
        for s1 in range(target, -1, -1):
            if dp[s1]:
                return S - 2 * s1
