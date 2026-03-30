class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        count = {}
        for j in nums:
            count[j] = 1 + count.get(j,0)
        for n,c in count.items():
            bucket[c].append(n)

        res = []
        for i in range(len(bucket)-1,0,-1):
            for a in bucket[i]:
                res.append(a)
                if len(res) == k:
                    return res
        