import heapq as hq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            hq.heappush(heap, num)
            if len(heap) > k:
                hq.heappop(heap)

        return heap[0]