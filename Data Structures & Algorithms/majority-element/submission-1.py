class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = len(nums)//2
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i,0)
        for j in freq:
            if freq[j]>major:
                return j