class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_1 ={}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in dict_1:
                return [dict_1[diff],i]
            dict_1[n] = i