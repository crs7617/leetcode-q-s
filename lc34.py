class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        f,l=-1,-1
        for i in range(len(nums)):
            if nums[i]==target:
                if f==-1:
                    f=i
                l=i
        return [f,l]
            
