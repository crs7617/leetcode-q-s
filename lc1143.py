class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l = len(text1)
        cache = [0] * l
        for let in text2:
            cnt = 0
            for i in range(l):
                if cnt < cache[i]:
                    cnt = cache[i]
                elif let == text1[i]:
                    cache[i] = cnt + 1
        return max(cache)
