class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Brute Force - nlogn
        # points.sort(key = lambda p: p[0]**2 + p[1]**2)
        # return points[:k]

        # Min-Heap - O(n+klogn)
        # min_heap = []
        # for x,y in points:
        #     dist = x**2 + y**2
        #     min_heap.append([dist,x,y])
        # heapq.heapify(min_heap)
        # res= []
        # while k > 0:
        #     dist,x,y = heapq.heappop(min_heap)
        #     res.append([x,y])
        #     k-=1
        # return res

        #Max- Heap - O(n logk)
        max_heap = []
        for x,y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(max_heap,[dist,x,y])
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        res = []
        while max_heap:
            dist,x,y = heapq.heappop(max_heap)
            res.append([x,y])
        return res
