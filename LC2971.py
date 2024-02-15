class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total_sum = sum(nums)
                
        for i in range(len(nums) - 1, 1, -1):
            total_sum -= nums[i]
            if total_sum > nums[i]:
                return total_sum + nums[i]
            
        return -1
