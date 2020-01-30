class Solution:
    def twoSumSmaller(self, nums: List[int], s: int, target: int) -> int:
        result = 0
        e = len(nums) -1
        
        while s < e:
            if nums[s] + nums[e] < target:
                result += e-s
                s = s +1
            else:
                e = e-1
        return result
            
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n, result = len(nums),0
        
        nums.sort()
        
        for i in range(n-2):
            result += self.twoSumSmaller(nums, i+1, target-nums[i])
            
        return result