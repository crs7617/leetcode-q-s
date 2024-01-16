class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums: return nums.index(target)
        nums.append(target)
        nums=sorted(nums)
        return nums.index(target)
         
        
