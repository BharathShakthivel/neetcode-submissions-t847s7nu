class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict ={}
        for i,v in enumerate(nums):
                diff = target - v
                if diff in my_dict:
                        return [my_dict[diff],i]
                my_dict[v] = i    
        return