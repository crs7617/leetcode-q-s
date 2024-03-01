class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s=sorted(s)
        s=s[:-1]
        s=s[::-1]
        s.append('1')
        return "".join(s)
