class Solution:
    def pivotSearch(self, nums, N):
        j = 0
        for i in range(N):
            if nums[i] <= 0:
                nums[i], nums[j] = nums[j], nums[i]
                j +=1
        return nums,j
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        nums, shift = self.pivotSearch(nums, N)
        
        nums = nums[shift:]
        size = N - shift
        for i in range(size):
            if ( abs(nums[i]) - 1 < size and nums[ abs(nums[i])-1] > 0):
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
                
        for i in range(size):
            if nums[i]>0:
                return i+1
            
        return size+1
        
        
