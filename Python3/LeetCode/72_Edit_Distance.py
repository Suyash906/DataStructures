class Solution:
    def minDistanceRecursive(self, word1: str, word2: str, l1: int, l2 :int) -> int:
        if 0 == l1:
            return l2
        if 0 == l2:
            return l1
        
        if word1[l1-1] == word2[l2-1]:
            return self.minDistanceUtil(word1, word2, l1-1, l2-1)
        else:
            return 1 + min(self.minDistanceUtil(word1, word2, l1, l2-1), 
                          self.minDistanceUtil(word1, word2, l1-1, l2),
                          self.minDistanceUtil(word1, word2, l1-1, l2-1))
        
    def minDistanceDP(self, word1: str, word2: str, l1: int, l2 :int) -> int:
        grid = [[ 0 for col in range(l2+1)] for row in range(l1+1)]
        
        for i in range(l1+1):
            for j in range(l2+1):
                if 0 == i:
                    grid[i][j] = j
                elif 0 == j:
                    grid[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    grid[i][j] = grid[i-1][j-1]
                else:
                    grid[i][j] = 1 + min(grid[i-1][j], grid[i][j-1], grid[i-1][j-1])
        return grid[l1][l2]
                
        
    def minDistance(self, word1: str, word2: str) -> int:
        # return self.minDistanceRecursive(word1, word2, len(word1), len(word2))
        return self.minDistanceDP(word1, word2, len(word1), len(word2))
        