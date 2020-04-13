class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlen = 0
        yaxis_map = {}
        yaxis_map[0] = -1
        count = 0
        for i, num in enumerate(nums):
            count = count + (1 if 1 == num else -1)
            if count in yaxis_map.keys():
                maxlen = max(maxlen, i - yaxis_map[count])
            else:
                yaxis_map[count] = i
        return maxlen