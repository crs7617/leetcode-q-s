import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(1,n+1):
            a = math.isqrt(i)
            dp[i] = min(dp[i-j**2] for j in range(1,a+1)) + 1
        return dp[-1]
