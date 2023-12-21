class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)+1
        t=(n*(n-1))//2

        for i in nums:
            t-=i

        return t
        
