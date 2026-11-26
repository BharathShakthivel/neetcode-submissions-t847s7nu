class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = height[0]
        max_right = height[len(height)-1]
        total_sum = 0
        prefix_max = [1] * len(height)
        suffix_max = [1] * len(height)
        for i in range(len(height)):
            if height[i] > max_left:
                max_left = height[i]
            prefix_max[i] = max_left
        for j in range(len(height)-1,-1,-1):
            if height[j] > max_right:
                max_right = height[j]
            suffix_max[j] = max_right
        for k in range(len(height)):
            total_sum+= (min(prefix_max[k],suffix_max[k])-height[k])
        return total_sum
        
