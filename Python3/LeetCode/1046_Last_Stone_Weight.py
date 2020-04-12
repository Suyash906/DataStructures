import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1 * stone)
        
        while len(heap) > 1:
            y = -1 * heapq.heappop(heap)
            x = -1 * heapq.heappop(heap)
            if x!=y:
                heapq.heappush(heap, -1 * (y-x))
        res = 0 if len(heap) <= 0 else -1 * heapq.heappop(heap)
        return res