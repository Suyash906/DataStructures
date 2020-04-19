class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m ==n and n ==1:
            return 1
        paths = [[0] * n] * m
        
        s = 0
        for i in range(1, n):
            paths[0][i] = 1
            
        s = 0
        for i in range(1, m):
            paths[i][0] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i][j-1] + paths[i-1][j]
        
        return paths[m-1][n-1]