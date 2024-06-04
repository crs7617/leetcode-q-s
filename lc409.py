class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        res=0
        y=0

        if len(c)==1:
            return c[s[0]]
        
        for i in c.values():
            if i>1:
                if i%2==0:
                    res+=i
                else:
                    res+=i-1
                    y+=1
            else:
                y+=1
        
        if y>0:
            res+=1
        
        return res
