class Solution:
    def climbStairs(self, n: int) -> int:
        a,b,c=0,1,0
        for i in range(n):
            c=a+b
            a,b=b,c
        
        return b

        
