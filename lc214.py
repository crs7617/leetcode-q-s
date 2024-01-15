class Solution(object):
    def shortestPalindrome(self, s):
        x=s[::-1]
        for i in range(len(x)):
            if s.startswith(x[i:]):
                return x[:i]+s
        
        return x+s
