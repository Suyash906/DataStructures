class Solution:
    def findFirstPosition(self, nums, target):
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] < target:
                    return mid
                else:
                    end = mid - 1
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid+1
        return -1
                
    def findLastPosition(self, nums, target):
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid+1] > target:
                    return mid
                else:
                    start = mid+1
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid+1
        return -1
                
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s_index = self.findFirstPosition(nums, target)
        e_index = self.findLastPosition(nums, target)
        return [s_index, e_index]