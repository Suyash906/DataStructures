# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0 # value to track next multiples of 2, 3 and 5
        while n > 1:
            # next multiples of 2, 3 and 5
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]
