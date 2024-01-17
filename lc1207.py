class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(Counter(a).values()) == len(set(Counter(a).values()))




        
