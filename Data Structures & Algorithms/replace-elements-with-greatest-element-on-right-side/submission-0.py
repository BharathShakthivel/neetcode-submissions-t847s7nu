class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [float("-inf")] * n
        ans[n-1] = arr[n-1]
        for j in range(n-2,-1,-1):
            ans[j] = max(ans[j+1], arr[j+1])
        ans[n-1] = -1
        return ans