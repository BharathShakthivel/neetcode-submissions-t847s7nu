class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        i,j = 0,len(nums)
        while j != len(ans):
            ans[i] = nums[i]
            ans[j] = nums[i]
            i+=1
            j+=1
        return ans