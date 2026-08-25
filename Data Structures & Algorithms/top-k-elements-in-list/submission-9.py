from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        groups = [[] for _ in range(len(nums))]

        for n, count in counts.items():
            groups[count - 1].append(n)

        result = []
        for group in groups[::-1]:
            for n in group:
                result.append(n)

                if len(result) == k:
                    return result

        return result
        