class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers) - 1
        
        while s < e:
            if numbers[s] + numbers[e] == target:
                return [s+1,e+1]
                s = s +1
            elif numbers[s] + numbers[e] > target:
                e = e-1
            else:
                s = s+1
        return []