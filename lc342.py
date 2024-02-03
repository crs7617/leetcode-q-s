class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n in [4**x for x in range(20)]

        
        
