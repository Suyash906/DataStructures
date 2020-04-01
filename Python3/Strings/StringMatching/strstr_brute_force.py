class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_len = len(needle)
        if n_len == 0:
            return 0
        h_len = len(haystack)
        
        for i,_ in enumerate(haystack):
            j=0
            while j < n_len and i+j < h_len and needle[j] == haystack[i+j]:
                j+=1
            if n_len == j:
                return i
        return -1