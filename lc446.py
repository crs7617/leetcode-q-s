class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        res=0
        dp=[defaultdict(int) for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                d=nums[i]-nums[j]
                dp[i][d] +=1 + dp[j][d]
                res+=dp[j][d]
        return res
        
