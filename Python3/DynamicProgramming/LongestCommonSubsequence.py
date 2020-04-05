class Solution:
    def longestCommonSubsequenceRecursive(self, text1, text2, l1, l2):
        if 0 == l1 or 0 == l2:
            return 0
        elif text1[l1-1] == text2[l2-1]:
            return 1 + self.longestCommonSubsequenceRecursive(text1, text2,l1-1,l2-1)
        else:
            return max(self.longestCommonSubsequenceRecursive(text1, text2, l1-1, l2), self.longestCommonSubsequenceRecursive(text1, text2, l1, l2-1))
        
    
    def longestCommonSubsequenceDP(self, text1, text2, l1, l2):
        
        grid = [[0] * (l2+1) for row in range(l1+1)]
        
        for i in range(l1+1):
            for j in range(l2+1):
                if 0 == i or 0 ==j:
                    grid[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    grid[i][j] = 1 + grid[i-1][j-1]
                else:
                    grid[i][j] = max(grid[i][j-1], grid[i-1][j])
        return grid[l1][l2]
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longestCommonSubsequenceDP(text1, text2, len(text1), len(text2))