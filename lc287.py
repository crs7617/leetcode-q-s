class Solution(object):
    def findDuplicate(self, nums):
        l=[0]*len(nums)
        for i in nums:
            l[i]+=1
            if l[i]==2:
                return i
        
