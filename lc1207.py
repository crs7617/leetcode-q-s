class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return Counter(Counter(arr).values()).most_common(1)[0][1]==1



        
