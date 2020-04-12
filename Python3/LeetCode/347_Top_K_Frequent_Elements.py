from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        
        countMap = Counter(nums)
        
        for key, val in countMap.items():
            if len(heap) <k:
                heapq.heappush(heap, (val, key))
            else:
                (ck, cv) = heap[0]
                if val > ck:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (val,key))
        res = []
        for i in range(k):
            curr = heapq.heappop(heap)
            res.append(curr[1])
        return res