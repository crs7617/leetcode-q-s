class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pt1 = 0
        pt2 = 1
        res = [0]*n
        for i in nums:
            if(i<0):
                res[pt2] = i
                pt2+=2
            else:
                res[pt1] = i
                pt1 +=2
        return res


        
