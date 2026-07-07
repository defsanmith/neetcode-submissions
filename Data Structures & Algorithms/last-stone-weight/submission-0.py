import heapq as hq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            hq.heappush(heap, -stone)

        while len(heap) > 1:
            x, y = -hq.heappop(heap), -hq.heappop(heap)

            if x != y:
                hq.heappush(heap, -(abs(x - y)))

        return -heap[0] if heap else 0
        