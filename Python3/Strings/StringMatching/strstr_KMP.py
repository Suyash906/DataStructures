class Solution:
    def getLPS(self, needle, n_len, lps):
        i = 1
        j = 0
        while i < n_len:
            if needle[i] == needle[j]:
                j += 1
                lps[i] = j
                i += 1
            elif j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
            
    def strStr(self, haystack: str, needle: str) -> int:
        n_len = len(needle)
        if n_len == 0:
            return 0
        h_len = len(haystack)
        lps  = [0] * n_len
        self.getLPS(needle, n_len, lps)
        i = j = 0
        while i < h_len:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == n_len:
                return i-j
            elif i < h_len and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
                
        return -1