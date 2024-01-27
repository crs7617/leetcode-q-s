class Solution:
    @cache
    def kInversePairs(self, n: int, k: int) -> int:
            return int(not k or n != 1 and (self.kInversePairs(n, k-1) + self.kInversePairs(n-1, k) - (k >= n and self.kInversePairs(n-1, k-n))) % 1_000_000_007)

        
