class Solution:
    def digSquareSum(self, n: int) -> int:
        s = 0
        while n:
            dig = n % 10
            s += dig * dig
            n = n // 10
        return s
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while slow != 1 or fast != 1:
            slow = self.digSquareSum(slow)
            fast = self.digSquareSum(fast)
            fast = self.digSquareSum(fast)
            if 1 != slow and slow == fast:
                return False
        return True
