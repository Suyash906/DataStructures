class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if 1 == numRows:
            return s
        
        cycle_len = 2 * numRows - 2
        n = len(s)
        res = ''
        for i in range(numRows):
            for j in range(0, n, cycle_len):
                if j+i >= n:
                    break
                res = res + s[i+j]
                if i != 0 and i != numRows-1 and j + cycle_len - i < n:
                    res = res + s[j + cycle_len - i]
        return res