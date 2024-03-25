class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[]
        c=Counter(nums)
        for i in range(1,n+1):
            if (c[i]>1): l.append(i)
        
        return l
        
