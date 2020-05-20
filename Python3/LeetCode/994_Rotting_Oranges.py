from collections import deque
class Solution:
    def getOrangeDivision(self, grid):
        fresh_orange_count = 0
        rotten_orange_list = []
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if 1 == col:
                    fresh_orange_count+=1
                if 2 == col:
                    rotten_orange_list.append((i,j))
        return (fresh_orange_count, rotten_orange_list)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        minutes = 1
        total_fresh_oranges, rotten_orange_list = self.getOrangeDivision(grid)
        if 0 == total_fresh_oranges:
            return 0
        visited = [[False for col in row] for row in grid]
        neighbours = [[0,1], [1,0], [-1,0], [0,-1]]
        row_max = len(grid)
        col_max = len(grid[0])
        
        
        q = deque()
        temp_q = deque()
        for orange in rotten_orange_list:
            q.append(orange)
        
        while q:
            x, y = q.popleft()
            visited[x][y] = True
            for neighbour in neighbours:
                n_x = neighbour[0] + x
                n_y = neighbour[1] + y
                if n_x >= 0 and n_x < row_max and n_y >= 0 and n_y < col_max and 1 == grid[n_x][n_y] and not visited[n_x][n_y]:
                    temp_q.append((n_x, n_y))
                    grid[n_x][n_y] = 2
                    visited[n_x][n_y] = True
                    total_fresh_oranges-=1
            if 0 == total_fresh_oranges:
                return minutes
            if not q:
                minutes+=1
                while temp_q:
                    q.append(temp_q.popleft())
        return minutes if 0 == total_fresh_oranges else -1
