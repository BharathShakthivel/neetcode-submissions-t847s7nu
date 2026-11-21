class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1,n):
            res[i] = nums[i-1] * res[i-1]
        right_product = 1
        for j in range(n-1,-1,-1):
            res[j] = res[j] * right_product
            right_product *= nums[j]
        return res