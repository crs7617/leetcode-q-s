class Solution(object):
    def maxSubArray(self, nums):
        maxsub=nums[0]
        sum=0

        for i in nums:
            if sum<0:
                sum=0
            sum+=i
            maxsub=max(sum,maxsub)
        
        return maxsub
        
