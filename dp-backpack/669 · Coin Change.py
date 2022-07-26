from typing import (
    List,
)

# dp-backpack, dp-coordinate
class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coin_change(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for j in coins:
                if (prev := i - j) >= 0 and dp[prev] != float('inf'):
                    dp[i] = min(dp[i], dp[prev] + 1)
        
        dp[amount] = dp[amount] if dp[amount] != float('inf') else -1

        return dp[amount]


# memory limit exceeded
class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coin_change(self, coins: List[int], amount: int) -> int:
        coins.sort()
        smallest = coins[0]
        memo = {}

        return self.dfs(coins, amount, smallest, memo)

    def dfs(self, coins, amount, smallest, memo):
        if amount == 0:
            return 0
        if amount < smallest:
            return -1

        if amount in memo:
            return memo[amount]

        res = float('inf')
        for coin in coins:
            if coin > amount:
                break
            r = self.dfs(coins, amount - coin, smallest, memo)
            if r != -1 and r + 1 < res:
                res = r + 1
        
        res = -1 if res == float('inf') else res

        memo[amount] = res
        return res
