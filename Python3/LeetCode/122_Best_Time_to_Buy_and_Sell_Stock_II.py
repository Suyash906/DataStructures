class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_len = len(prices)
        if 0 == p_len:
            return 0
        i = 0
        max_profit = 0
        peak = valley = prices[0]
        while i < p_len-1:
            while i < p_len-1 and prices[i] >= prices[i+1]:
                i+=1
            valley = prices[i]
            while i < p_len-1 and prices[i] <= prices[i+1]:
                i+=1
            peak = prices[i]
            max_profit += (peak-valley)
        return max_profit