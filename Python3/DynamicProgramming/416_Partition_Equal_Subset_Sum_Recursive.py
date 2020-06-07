class Solution:
    def canPartitionUtil(self, nums, index, tot_sum, curr_sum):
        if index >= len(nums):
            return False
        if tot_sum == curr_sum * 2:
            return True
        case_1 = self.canPartitionUtil(nums, index+1, tot_sum, curr_sum+nums[index])
        case_0 = self.canPartitionUtil(nums, index+1, tot_sum, curr_sum)
        return  case_0 or case_1
    def canPartition(self, nums: List[int]) -> bool:
        return self.canPartitionUtil(nums, 0, sum(nums), 0)
