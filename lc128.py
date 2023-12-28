class Solution(object):
    def longestConsecutive(self, nums):
        sets=set(nums)
        longest=0

        for i in nums:
            if (i-1) not in sets:
                length=0
                while(i+length) in sets:
                    length+=1
                longest=max(length,longest)
        return longest

        
