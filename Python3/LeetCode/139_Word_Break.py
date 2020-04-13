class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_len = len(s)
        memo = [False] * (s_len + 1)
        memo[0] = True
        wordDict = set(wordDict)
        for i in range(1, s_len+1):
            for j in range(i):
                if s[j:i] in wordDict and memo[j]:
                    memo[i] = True
                    break
        return memo[s_len]