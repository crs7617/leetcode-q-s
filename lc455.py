class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i=j=0

        while i<len(g):
            while j<len(s) and g[i]>s[j]:
                j+=1
            if j==len(s):
                break
            
            i+=1
            j+=1
        return i
        
