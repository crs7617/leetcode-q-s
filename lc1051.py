class Solution:
    def heightChecker(self, h: List[int]) -> int:
        return sum(sorted(h)[i]!=h[i] for i in range(len(h)))
