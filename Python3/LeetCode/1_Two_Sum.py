class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for index,value in enumerate(nums):
            curr = target-value
            if value in complement.keys():
                return [complement[value], index]
            else:
                complement[curr] = index
        return []
