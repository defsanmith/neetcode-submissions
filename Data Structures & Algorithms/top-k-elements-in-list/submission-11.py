class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]

        counts = Counter(nums)


        for n, count in counts.items():
            buckets[count].append(n)

        result = []
        buckets.reverse()
        for bucket in buckets:
            for n in bucket:
                result.append(n)

                if len(result) == k:
                    return result

        return result