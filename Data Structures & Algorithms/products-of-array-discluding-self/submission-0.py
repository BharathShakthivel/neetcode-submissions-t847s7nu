class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1]
        right_product = 1
        for j in range(n-1,-1,-1):    
            prefix[j] = prefix[j] * right_product
            right_product*=nums[j]
        return prefix