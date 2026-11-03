class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = 1
        nums =set(nums)
        while True:
            if n not in nums:
                return n
            n+=1