from typing import (
    List,
)

# 指针交换型滚动数组
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [0] * 3
        dped = [0] * 3

        for i in range(1, n + 1):
            for j in range(3):
                dped[j] = min(dp[(j + 1) % 3], dp[(j + 2) % 3]) + costs[i - 1][j]
            dp, dped = dped, dp
        
        return min(dp)


class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0] * 3 for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(3):
                dp[i][j] = costs[i - 1][j] + min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])
        
        return min(dp[n])


# not recommended, 太多次取模运算，浪费算力
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0] * 3 for _ in range(2)]

        for i in range(1, n + 1):
            for j in range(3):
                dp[i % 2][j] = min(dp[(i - 1) % 2][(j + 1) % 3], dp[(i - 1) % 2][(j + 2) % 3]) + costs[i - 1][j]
        
        return min(dp[n % 2])


class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[float('inf')] * 3 for _ in range(n + 1)]
        
        for j in range(3):
            dp[0][j] = 0

        for i in range(1, n + 1):
            for j in range(3):
                for k in range(3):
                    if k == j:
                        continue
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[i - 1][j])
        
        return min(dp[n])


# dfs, memoized search
# just for research, do not use it
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs: List[List[int]]) -> int:
        def dfs(costs, ith, color):
            if ith == len(costs):
                return 0

            if memo[ith][color] != -1:
                return memo[ith][color]

            right = float('inf')
            for j in range(3):
                if j == color:
                    continue
                right = min(right, dfs(costs, ith + 1, j))
            
            res = costs[ith][color] + right

            memo[ith][color] = res
            return res
        
        memo = [[-1] * 3 for _ in range(len(costs))]

        return min(dfs(costs, 0, i) for i in range(3))

