class Solution:
    def numSubarraysWithSum(self, a: List[int], g: int) -> int:
        result = 0
        z, s = Counter([0]), 0
        for v in a:
            s += v
            result += z[s-g]
            z[s] += 1

        return result
