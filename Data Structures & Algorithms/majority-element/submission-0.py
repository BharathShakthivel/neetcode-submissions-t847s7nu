class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = len(nums)//2
        majority_element_dict = {}
        for i in nums:
            majority_element_dict[i] = 1 + majority_element_dict.get(i,0)
        for j in majority_element_dict:
            if majority_element_dict[j] > major:
                return j
