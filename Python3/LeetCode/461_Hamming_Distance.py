class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = bin(x^y).replace("0b","")
        count = 0
        for char in xor:
            if '1' == char:
                count += 1
        return count