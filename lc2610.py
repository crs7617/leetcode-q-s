class Solution(object):
    def findMatrix(self, nums):
        count=defaultdict(int)
        res=[]


        for i in nums:
            rows=count[i]
            if len(res)==rows:
                res.append([])
            res[rows].append(i)
            count[i]+=1

        return res

        
