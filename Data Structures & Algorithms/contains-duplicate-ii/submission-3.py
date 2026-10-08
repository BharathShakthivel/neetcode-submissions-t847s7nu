class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        hash_set = set()
        n = len(nums)
        for r in range(n):
            if (r - l) > k:
                hash_set.remove(nums[l])
                l+=1
            if nums[r] in hash_set:
                return True
            hash_set.add(nums[r])
        return False
