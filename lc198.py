class Solution:
    def rob(self, nums: List[int]) -> int:
        y,n=0,0
        for i in nums:
            a=n+i
            b=max(y,n)
            y,n=a,b
        return max(y,n)
        
