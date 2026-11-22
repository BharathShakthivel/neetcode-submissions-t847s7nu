class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            count[i] = 1 + count.get(i,0)
        for i,v in count.items():
            freq[v].append(i)
        res = []
        for j in range(len(freq)-1,0,-1):
            for l in freq[j]:
                res.append(l)
                if len(res)==k:
                    return res
