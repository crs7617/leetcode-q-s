class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        temp = []
        while s:
            temp.append(s[:k])
            s = s[k:]
        for i in range(0, len(temp), 2):
            temp[i] = temp[i][::-1]
        return ''.join(temp)

        
