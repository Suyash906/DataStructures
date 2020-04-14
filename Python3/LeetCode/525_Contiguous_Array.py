class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Track all the unique values of count in yaxis_map with the least index
        # If the count value is same at multipe index, it indicates that the number of 0 and 1 are same
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