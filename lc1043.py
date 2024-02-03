class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            curmax, best = 0, 0
            for t in range(1, k + 1):
                if t<= i:
                    curmax = max(curmax, arr[i - t])
                    best = max(best, dp[i - t] + curmax * t)
            dp[i] = best 
        return dp[n]
