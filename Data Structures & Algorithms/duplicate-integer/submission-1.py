class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_duplicate = set()
        for i in nums:
            if i in has_duplicate:
                return True
            has_duplicate.add(i)
        return False

            