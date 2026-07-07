import heapq as hq
from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            hq.heappush(heap, (-distance, [x, y]))
            if len(heap) > k:
                hq.heappop(heap)

        return [point for distance, point in heap]