import heapq as hq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        buckets = [[] for _ in range(len(nums))]
        for num, count in counts.items():
            buckets[count - 1].append(num)

        result = []
        for bucket in buckets[::-1]:
            for n in bucket:
                result.append(n)
                if len(result) == k:
                    return result

        return result