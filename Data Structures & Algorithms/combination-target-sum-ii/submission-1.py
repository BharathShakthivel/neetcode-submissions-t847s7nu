class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol = [],[]
        candidates.sort()
        n = len(candidates)

        def backtrack(i,total):
            if total == target:
                res.append(sol[:])
                return
            if i == n or total > target:
                return
            for j in range(i,n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j]> (target - total):
                    break
                sol.append(candidates[j])
                backtrack(j+1,total + candidates[j])
                sol.pop()
        backtrack(0,0)
        return res