class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        pq = []
        for i in range(n - 1):
            height_diff = heights[i + 1] - heights[i]
            if height_diff > 0:
                heapq.heappush(pq, height_diff)
                if len(pq) > ladders:
                    bricks -= heapq.heappop(pq)
                if bricks < 0:
                    return i
        return n - 1
        
