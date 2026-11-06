class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res= 0
        for n in nums:
            res = res | n
        return res << (len(nums)-1)