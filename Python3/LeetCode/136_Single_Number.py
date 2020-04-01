class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for curr in nums:
            res = res ^ curr
        return res