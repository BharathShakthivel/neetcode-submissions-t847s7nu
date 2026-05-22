class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS - Breadth First Search
        from collections import deque
        q = deque()
        visited = set()
        
        # Helper Function
        def add_room (r,c):
            if r >=len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or (r,c) in visited or grid[r][c] == -1:
                return
            visited.add((r,c))
            q.append((r,c))
        # We add all the treasure points in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        # Starting point of the treasure, we set the value again to zero in out first iteration
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                add_room(r+1,c)
                add_room(r,c+1)
                add_room(r-1,c)
                add_room(r,c-1)
            dist+=1

