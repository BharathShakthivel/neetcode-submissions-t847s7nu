class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Brute Force
        nums.sort()
        sol,res = [],[]
        n = len(nums)
        def backtrack(start):
            res.append(sol[:])            
            for i in range(start,n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                sol.append(nums[i])
                backtrack(i+1)
                sol.pop()

        backtrack(0)
        return res