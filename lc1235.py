class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        x=sorted(zip(startTime,endTime,profit))
        cache={}
        def dfs(i):
            if (i==len(x)):
                return 0
            
            if i in cache:
                return cache[i]
            
            res=dfs(i+1)

            j=bisect.bisect(x,(x[i][1],-1,-1))
            cache[i]=res=max(res,x[i][2]+dfs(j))
            return res
        
        return dfs(0)
