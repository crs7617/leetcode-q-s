class Solution:
    def findLeastNumOfUniqueInts(self, a: List[int], k: int) -> int:
        return len(c:=Counter(a))-sum((k:=k-v)>=0 for v in sorted(c.values()))
