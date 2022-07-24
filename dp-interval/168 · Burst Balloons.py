from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def max_coins(self, nums: List[int]) -> int:
        if not nums:
            return 0

        a = [1, *nums, 1]
        n = len(a)
        
        # dp[i][i + 1] = 0
        dp = [
            [0] * n
            for _ in range(n)
        ]

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + a[i] * a[k] * a[j]
                    )
        
        return dp[0][n - 1]


class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def max_coins(self, nums: List[int]) -> int:
        if not nums:
            return 0

        a = [1, *nums, 1]
        n = len(a)
        
        dp = [
            [0] * n
            for _ in range(n)
        ]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + a[i] * a[k] * a[j]
                    )
        
        return dp[0][n - 1]
