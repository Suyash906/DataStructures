### Coin Change
```
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
```
```
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:return 0
        
        memo = [0 for i in range(amount+1)]
        
        for i in range(1, amount+1):
            min_coin_count = float(inf)
            for coin in coins:
                if coin <= i:
                    min_coin_count = min(min_coin_count, 1 + memo[i-coin])
            memo[i] = min_coin_count
        
        if min_coin_count == float(inf):
            return -1
                
        return memo[amount]
```

---

### Coin Change - 2
```
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for col in range(amount+1)] for row in range(len(coins)+1)]
        
        # we can make the amount 0 by not choosing any of the coin
        
        for i in range(len(coins)+1):
            dp[i][0] = 1
        
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
        return dp[len(coins)][amount]
```
---

### Regular Expression Match
```
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp  = [[False for col in range(len(p)+1)] for row in range(len(s)+1)]
        
        dp[0][0] = True
        
        for i in range(1, len(p)+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
                
                
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] != '*':
                    if p[j-1] == '.' or s[i-1] == p[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                else:
                    # case 0
                    dp[i][j] = dp[i][j-2]
                    
                    # case 1
                    # check if preceding character in p matches current char in s
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                        
        return dp[len(s)][len(p)]
```

---

### Wildcard Matching
```
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        if not s and not p:return True
        
        if s and not p:return False
        
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        
        dp[0][0] = True
        
        index = 0
        while index < len(p) and p[index] == '*':
            dp[0][index+1] = True
            index+=1
        
        if index == len(p):return True
            
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # dp[i][j-1] - * mattches with zero chararcters
                    # dp[i-1][j] - * mattches with one or more chararcters
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        return dp[len(s)][len(p)]
```
---

### Knight Probablity in ChessBoard
```
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        dp = [[0 for _ in range(N)] for _ in range(N)]
        dp[r][c] = 1
        
        directions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        
        for curr in range(K):
            dp2 = [[0 for _ in range(N)] for _ in range(N)]
            for i, row in enumerate(dp):
                for j, col in enumerate(row):
                    for dx, dy in directions:
                        nx = i+dx
                        ny = j+dy
                        if nx >= 0  and nx < N and ny >= 0 and ny < N:
                            dp2[nx][ny] += col/8
            dp = dp2
        res = 0.0
        for row in dp:
            for col in row:
                res+=col
        return res
```
---

### Knight Dialer
```
class Solution(object):
    def knightDialer(self, N):
        MOD = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        dp = [1] * 10
        for hops in range(N-1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD
```
---
### Buy and Sell Stock
```
class Solution {
    public int maxProfit(int[] prices) {
        int len = prices.length;
        if(0 == len)
            return 0;
        int i, j, min, max=0;
        min = prices[0];
        for(i = 1 ; i < len ; i++){
            if(prices[i]>min)
                max = Math.max(max, prices[i] - min);
            else
                min = prices[i];
        }
        return max;
    }
}
```

### Buy and sell stock ii
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:return 0
        i = 0
        j = 0
        n = len(prices)
        res = 0
        while i < n-1 and j < n:
            while i < n-1 and prices[i] > prices[i+1]:
                i+=1
            valley = prices[i]
            j = i+1
            while j < n-1 and prices[j] < prices[j+1]: 
                j+=1
            if j == n:
                 return res
            peak = prices[j]
            i=j+1
            res+= (peak-valley)
        return res
```

### Buy and sell stock iv
```
    public int maxProfitSlowSolution(int prices[], int K) {
        if (K == 0 || prices.length == 0) {
            return 0;
        }
        int T[][] = new int[K+1][prices.length];

        for (int i = 1; i < T.length; i++) {
            for (int j = 1; j < T[0].length; j++) {
                int maxVal = 0;
                for (int m = 0; m < j; m++) {
                    maxVal = Math.max(maxVal, prices[j] - prices[m] + T[i-1][m]);
                }
                T[i][j] = Math.max(T[i][j-1], maxVal);
            }
        }
        printActualSolution(T, prices);
        return T[K][prices.length - 1];
    }
```
