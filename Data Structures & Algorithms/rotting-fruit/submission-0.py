class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        fresh = 0
        time = 0
        ROWS,COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j] ==2:
                    q.append((i,j))
        if not fresh:
            return 0
        def all_directions(i,j):
            nonlocal fresh
            if i>= ROWS or j >= COLS or i <0 or j<0 or grid[i][j]==0 or grid[i][j]==2:
                return
            grid[i][j]=2
            fresh-=1
            q.append((i,j))
        
        while q:
            for _ in range(len(q)):
                row,col = q.popleft()
                grid[row][col] = 2
                all_directions(row+1,col)
                all_directions(row,col+1)
                all_directions(row-1,col)
                all_directions(row,col-1)
            if q:
                time+=1
        if fresh>0:
            return -1
        return time

        