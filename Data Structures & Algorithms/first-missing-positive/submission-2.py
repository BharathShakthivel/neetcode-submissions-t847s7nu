class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # min_num = float("inf")
        # for i in nums:
        #     min_num = min(min_num,i)

        # while True:
        #     if min_num in set(nums):
        #         min_num+=1
        #         if min_num not in set(nums):
        #             return min_num        

        n = 1
        while True:
            if n not in set(nums):
                return n
            n+=1