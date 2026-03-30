class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        If 0 → swap with low, low++, mid++
        If 1 → mid++
        If 2 → swap with high, high--
        """
        
        l = 0
        r = len(nums)-1
        i = 0
        def swap (x,y):
            temp = nums[x]
            nums[x] = nums[y]
            nums[y] = temp
        
        while i<=r:
            if nums[i] == 0:
                swap(l,i)
                l+=1
            elif nums[i] == 2:
                swap(i,r)
                r-=1
                i-=1
            i+=1
        return nums

            
