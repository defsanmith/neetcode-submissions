from collections import Counter, deque
import heapq as hq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-count for task, count in Counter(tasks).items()]
        hq.heapify(heap)

        q = deque([])

        time = 0
        while heap or q:
            time += 1

            if q and q[0][1] <= time:
                hq.heappush(heap, q.popleft()[0])

            # if not heap:
            #     time = q[0][1]
            if heap:
                count = 1 + hq.heappop(heap)
                if count < 0:
                    q.append((count, time + n + 1))
            

            
        return time