class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # Intuition:
        # We want to XOR N's binary with an array of 1's of the same length.
        if 0 == N:
            return 1
        if 1 == N:
            return 0
        x = 1
        while x <= N:
            x = x << 1 # x*=2
        return N ^ (x-1)
