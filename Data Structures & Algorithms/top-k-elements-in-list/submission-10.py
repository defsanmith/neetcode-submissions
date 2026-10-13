import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = []
        for n, count in counts.items():
            hq.heappush(heap, [-count, n])

        result = []
        for _ in range(k):
            result.append(hq.heappop(heap)[1])

        return result