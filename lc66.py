class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = int("".join([str(i) for i in digits])) + 1
        res = [int(i) for i in str(sum)]
        return res






        
