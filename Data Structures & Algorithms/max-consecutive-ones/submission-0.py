class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        run_count = 0
        for i in nums:
            if i == 1:
                run_count+=1
                max_count = max(max_count,run_count)
            else:
                run_count=0
        return max_count