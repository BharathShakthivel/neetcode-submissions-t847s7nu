class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        l,r = 0,1
        prev = ""
        n = len(arr)
        while r<n:
            if prev!= ">" and arr[r-1] > arr[r]:
                prev = ">"
                res = max(res, (r-l+1))
                r+=1
            elif prev!= "<" and arr[r-1] < arr[r]:
                prev = "<"
                res = max(res, (r-l+1))
                r+=1
            else:
                if arr[r-1] == arr[r]:
                    r = r+1
                l = r-1
                prev = ""
        return res
