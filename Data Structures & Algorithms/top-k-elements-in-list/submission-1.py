class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for i in nums:
            count[i] = 1 + count.get(i,0)
        freq =[[] for j in range(len(nums)+1)]
        for n,c in count.items():
            freq[c].append(n)
        for l in range(len(freq)-1,-1,-1):
            for m in freq[l]:
                res.append(m)
                if len(res)==k:
                    return res