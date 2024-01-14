class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        f1 = [0] * 26
        f2 = [0] * 26

        for ch in word1:
            f1[ord(ch) - ord('a')] += 1

        for ch in word2:
            f2[ord(ch) - ord('a')] += 1

        for i in range(26):
            if (f1[i] == 0 and f2[i] != 0) or (f1[i] != 0 and f2[i] == 0):
                return False

        f1.sort()
        f2.sort()

        for i in range(26):
            if f1[i] != f2[i]:
                return False

        return True

        
