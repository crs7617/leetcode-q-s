class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        res = list(set(nums))
        res.sort(reverse = True)
        if len(res) >= 3:
            return res[2]
        return max(res)
