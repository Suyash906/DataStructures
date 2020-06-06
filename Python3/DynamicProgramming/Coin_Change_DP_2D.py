class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount<0:return 0
        
        INFINITY = amount+1
        dp =  [[ 0 for col in range(amount+1)] for row in range(len(coins)+1)]
        
        # if amount == 0,  the num of coins is zero
        for i in range(amount+1):
            dp[0][i] = INFINITY
        
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    case_0 = dp[i-1][j]
                    case_1 = 1 + dp[i][j-coins[i-1]]
                    dp[i][j] = min(case_0, case_1)
        res = dp[len(coins)][amount]
        return res if res != INFINITY else -1 
