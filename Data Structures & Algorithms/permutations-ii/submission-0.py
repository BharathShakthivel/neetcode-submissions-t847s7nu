class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res,sol = [],[]
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        def backtrack():
            if len(sol) == len(nums):
                res.append(sol.copy())
                return
            for n in count:
                if count[n] > 0:
                    sol.append(n)
                    count[n]-=1
                    backtrack()
                    count[n]+=1
                    sol.pop()
        backtrack()
        return res        