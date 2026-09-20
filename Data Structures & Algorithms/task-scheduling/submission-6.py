class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import deque
        Count = Counter(tasks)
        max_heap = [-s for s in Count.values()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0
        while max_heap or q:
            time+=1
            if max_heap:
                cur = 1 + heapq.heappop(max_heap)
                if cur:
                    q.append([cur,time+n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap,q.popleft()[0])
        return time
