class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return[i,j]
        
        # Optimal
        hash_map = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hash_map:
                return [hash_map[diff],i]
            hash_map[n] = i
        