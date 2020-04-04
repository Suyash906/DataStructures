class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzeroIndex = 0
        for num in nums:
            if num!=0:
                nums[nonzeroIndex] = num
                nonzeroIndex += 1
        for i in range(nonzeroIndex, len(nums)):
            nums[i] = 0