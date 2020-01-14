class Solution:
    def hammingWeight(self, n: int) -> int:
        binval = bin(n).replace("0b","")
        count = 0
        for curr in binval:
            if '1' == curr:
                count += 1
            
        return count
        