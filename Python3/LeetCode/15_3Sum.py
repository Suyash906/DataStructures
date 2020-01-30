class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result, n = [], len(nums)
        nums.sort()
        for i in range(n):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = nums[i] * -1
            
            s = i+1
            e = n-1
            while s<e:
                if nums[s] + nums[e] == target:
                    result.append([nums[i],nums[s],nums[e]])
                    s=s+1
                    while s<e and nums[s] == nums[s-1]:
                        s=s+1
                elif nums[s] + nums[e] < target:
                    s = s +1
                else:
                    e = e-1
        return result