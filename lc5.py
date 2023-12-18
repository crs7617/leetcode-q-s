class Solution(object):
    def longestPalindrome(self, s):
        if len(s)<=1:
            return s

        maxl=1
        maxs=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if (j-i+1)>maxl and s[i:j+1]== s[i:j+1][::-1]:
                    maxl=j-i+1
                    maxs=s[i:j+1]

        return maxs
        
