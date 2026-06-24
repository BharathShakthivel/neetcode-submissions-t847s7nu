class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Brute Force
        '''
        # Sort first. Backtrack and build subsets.
        # Skip duplicates at same recursion level (i > start and same value).
        # Choose -> recurse -> backtrack.
        '''
        # nums.sort()
        # sol,res = [],[]
        # n = len(nums)
        # def backtrack(start):
        #     res.append(sol[:])            
        #     for i in range(start,n):
        #         if i > start and nums[i] == nums[i-1]:
        #             continue
        #         sol.append(nums[i])
        #         backtrack(i+1)
        #         sol.pop()

        # backtrack(0)
        # return res

        
        
        nums.sort()
        sol,res = [],[]
        n = len(nums)
        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return         
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
            while i+1 < n and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1)
        backtrack(0)
        return res