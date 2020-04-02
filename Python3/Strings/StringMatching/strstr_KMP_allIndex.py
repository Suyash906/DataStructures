class Solution:
    def getPrefixTable(self, needle, n_len, prefixtable):
        i = 1
        j = 0

        while i < n_len:
            if needle[i] == needle[j]:
                j += 1
                prefixtable[i] = j
                i+=1
            elif j != 0:
                j = prefixtable[j-1]
            else:
                i+=1


    def KMPSearch(self, haystack, needle):
        n_len = len(needle)
        h_len = len(haystack)
        prefixtable = [0] * n_len
        self.getPrefixTable(needle, n_len, prefixtable)
        i = 0
        j = 0
        next_i=0
        res = []
        while i < h_len:
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            
            if j == n_len:
                res.append(i-j)
                j = prefixtable[j-1]
                if prefixtable[j] !=0:
                    next_i += 1
                    i = next_i
                j = 0

            elif i < h_len and haystack[i] != needle[j]:
                if j != 0:
                    j = prefixtable[j-1]
                else:
                    i += 1

        return [-1] if len(res) == 0 else res

if __name__=='__main__': 
    print('Testcase : 1 - Only 1 occurence of pattern')
    haystack = "ABABDABACDABABCABAB"
    needle = "ABABCABAB"
    print("All the positions of the patterns are ", Solution().KMPSearch(haystack, needle))

    print('Testcase : 2 - No occurence of pattern')
    haystack = "ABABDABACDABABCABA"
    needle = "ABABCABAB"
    print("All the positions of the patterns are ", Solution().KMPSearch(haystack, needle))

    print('Testcase : 3 - Multiple occurence of pattern')
    haystack = "AAAAAAAAAAAAAAAA"
    needle = "A"
    print("All the positions of the patterns are ", Solution().KMPSearch(haystack, needle))