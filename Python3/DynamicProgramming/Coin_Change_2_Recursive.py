class Solution:
    def changeUtil(self, amount, coins, index):
        # base
        if amount < 0 or index >= len(coins):
            return 0
        if amount == 0:
            return 1
        
        # body
        case_0 = self.changeUtil(amount, coins, index+1)
        case_1 = self.changeUtil(amount - coins[index], coins, index)
        
        return case_0 + case_1
        
    def change(self, amount: int, coins: List[int]) -> int:
        if amount==0:return 1
        return self.changeUtil(amount, coins, 0)
        
