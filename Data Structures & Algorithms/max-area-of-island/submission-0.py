class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area =0
        if not grid:
            return 0
        def dfs(i,j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j <0 or grid[i][j] == 0:
                return 0
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            area = 1
            area+= dfs(i+1,j)
            area+= dfs(i,j+1)
            area+= dfs(i-1,j)
            area+= dfs(i,j-1)
            return area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i,j) not in visited:
                    max_area = max(max_area,dfs(i,j))
        return max_area