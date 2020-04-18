class Solution:
    def dfs(self, grid, x,y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != '1':
            return
        grid[x][y] = '#'
        self.dfs(grid,x+1, y)
        self.dfs(grid,x, y+1)
        self.dfs(grid,x-1, y)
        self.dfs(grid,x, y-1)
            
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:return 0
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if '1' == grid[i][j]:
                    self.dfs(grid, i, j)
                    count += 1
        return count