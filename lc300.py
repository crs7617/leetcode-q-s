class Solution(object):
    def lengthOfLIS(self, nums):
        l=[1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    l[i]=max(l[i],1+l[j])
        return max(l)
        
