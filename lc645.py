class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res=[0,0]
        c=Counter(nums)
        for i in range(1,len(nums)+1):
            if c[i]==0:
                res[1]=i
            if c[i]==2:
                res[0]=i
        return res
        
