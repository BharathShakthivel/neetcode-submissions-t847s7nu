class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        sol,res = [],[]


        def backtrack(nums):
            if len(nums) == 0:
                res.append(sol[:])
                return
            
            for j in range(len(nums)):
                sol.append(nums[j])
                element = nums.pop(j)
                backtrack(nums)
                sol.pop()
                nums.insert(j,element)
        backtrack(nums)
        return res