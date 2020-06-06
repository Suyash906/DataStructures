class Solution:
    def coinChangeUtil(self, coins, amount, index, coin_count):
        # base 
        if 0 == amount:
            return coin_count
        if index >= len(coins) or amount<0:
            return -1
        
        # body
        case_0 = self.coinChangeUtil(coins, amount, index+1, coin_count)
        
        case_1 = self.coinChangeUtil(coins, amount-coins[index], index, coin_count+1)
        
        if -1 == case_0:
            return case_1
        if -1 == case_1:
            return case_0
            
        return min(case_0, case_1)
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        return self.coinChangeUtil(coins, amount, 0 , 0) 
