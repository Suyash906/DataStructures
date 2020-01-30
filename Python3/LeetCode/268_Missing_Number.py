class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        checkList = [0] * (len(nums)+1)
        
        for ele in nums:
            checkList[ele] = 1
        print(checkList)
        for index,ele in enumerate(checkList):
            if 0 == ele:
                return index
        return 0