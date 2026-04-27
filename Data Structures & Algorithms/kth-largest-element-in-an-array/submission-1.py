class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Brute Force
        # nums.sort()
        # return nums[-k]

        # Max_heap
        max_heap = [-p for p in nums]
        heapq.heapify(max_heap)
        res = 0
        for i in range(k):
            res = heapq.heappop(max_heap)
        return -res