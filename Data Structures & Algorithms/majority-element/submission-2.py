class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # major = len(nums)//2
        # freq = {}
        # for i in nums:
        #     freq[i] = 1 + freq.get(i,0)
        # for j in freq:
        #     if freq[j]>major:
        #         return j


        # Follow up (O(n))
        res,count = 0,0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res
            