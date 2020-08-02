class Solution:
    def longestCommonSubsequenceDP(self, s1, s2):
        l1 = len(s1)+1
        l2 = len(s2)+1
        
        dp = [[0 for _ in range(l2)] for _ in range(l1)]
        
        for i in range(1, l1):
            for j in range(1,l2):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[l1-1][l2-1]
    def longestCommonSubsequenceRecursive(self, s1, s2, i, j):
        ## base
        if i >= len(s1) or j >= len(s2):
            return 0

        ## body

        if s1[i] == s2[j]:
            return 1 + self.longestCommonSubsequenceRecursive(s1,s2,i+1,j+1)

        case_1 = self.longestCommonSubsequenceRecursive(s1,s2,i,j+1)

        case_2 = self.longestCommonSubsequenceRecursive(s1,s2,i+1,j)

        case_3 = self.longestCommonSubsequenceRecursive(s1,s2,i+1,j+1)

        return max(case_1, case_2, case_3)
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # return self.longestCommonSubsequenceRecursive(text1, text2, 0, 0)
        return self.longestCommonSubsequenceDP(text1, text2)
