import heapq as hq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = []
        for num, count in counts.items():
            hq.heappush(heap, (count, num))
            if len(heap) > k:
                hq.heappop(heap)

        return [num for count, num in heap]