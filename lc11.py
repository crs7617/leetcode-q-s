class Solution(object):
    def maxArea(self, height):
        l,r=0,len(height)-1
        res=0
        while l<r:
            a=(r-l)*min(height[l],height[r])
            res=max(res,a)
            
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        
        return res
