class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return reduce(lambda x, y: x & y, map(Counter, words)).elements()
        
