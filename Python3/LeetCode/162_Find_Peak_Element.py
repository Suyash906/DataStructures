class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        numslen = len(nums)
        
        if 1 == numslen:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        
        if nums[numslen-1] > nums[numslen-2]:
            return (numslen-1)
        
        
        start =1
        end = numslen -2
        
        while start <= end:
            mid  = (start + end) // 2
            
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                end = mid-1
            else:
                start = mid+1