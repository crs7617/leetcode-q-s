
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('AEIOUaeiou')
        count = 0
        mid_index = len(s) // 2

        for i in range(mid_index):
            a = s[i]
            b = s[mid_index + i]
            if a in vowels:
                count += 1
            if b in vowels:
                count -= 1

        return count == 0
