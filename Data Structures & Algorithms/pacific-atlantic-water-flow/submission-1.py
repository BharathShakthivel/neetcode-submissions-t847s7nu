class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # TIME - O (m x n)
        # Required Space:
        result = []
        ROWS,COLS = len(heights),len(heights[0])
        # We create 2 sets to keep track of corresponding visited Nodes
        atlantic_set = set()
        pacific_set = set()

        # Depth First Search Algorithm (Contains row,col,visit,prev)
        def dfs(i,j,visit,prev):
            if (i,j) in visit or i < 0 or j < 0 or i == ROWS or j == COLS or heights[i][j] < prev:
                return
            visit.add((i,j))
            dfs(i+1,j,visit,heights[i][j])
            dfs(i,j+1,visit,heights[i][j])
            dfs(i-1,j,visit,heights[i][j])
            dfs(i,j-1,visit,heights[i][j])
        
        # We go through each Cols for both oceans to check if it is reachable paths
        for c in range(COLS):
            dfs(0,c,pacific_set,heights[0][c])
            dfs(ROWS-1,c,atlantic_set,heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r,0,pacific_set,heights[r][0])
            dfs(r,COLS-1,atlantic_set,heights[r][COLS-1])
        # We go through each cell to find if it is reachable by both oceans,if so we add it to the result
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pacific_set and (i,j) in atlantic_set:
                    result.append((i,j))
        return result
        