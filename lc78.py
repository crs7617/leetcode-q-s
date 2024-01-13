class Solution(object):
    def subsets(self, nums):
        l1=[[]]
        for i in range(1,2**len(nums)):
            l2=[]
            for j in range(len(nums)):
                if(i&1<<j):
                    l2.append(nums[j])
            l1.append(l2)
        return l1
