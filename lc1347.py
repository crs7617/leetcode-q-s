class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = [0] * 26
        i = 0

        while i < len(s):
            count[ord(t[i]) - ord('a')] += 1
            count[ord(s[i]) - ord('a')] -= 1
            i += 1

        ans = 0
        i = 0

        while i < 26:
            ans += max(0, count[i])
            i += 1

        return ans

