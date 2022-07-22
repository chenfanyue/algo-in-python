from typing import (
    List,
)

# 区间起点从右往左，区间终点从区间起点往右
class Solution:
    """
    @param a: An integer array
    @return: An integer
    """
    def stone_game(self, a: List[int]) -> int:
        if not a:
            return 0

        n = len(a)
        prefix = [0] * (n + 1)
        for i in range(len(a)):
            prefix[i + 1] = prefix[i] + a[i]

        # dp = [
        #     [float('inf')] * n
        #     for _ in range(n)
        # ]

        # for i in range(n):
        #     dp[i][i] = 0
        dp = [
            [0] * n
            for _ in range(n)
        ]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                state = float('inf')
                for k in range(i, j):
                    state = min(state, dp[i][k] + dp[k + 1][j])
                dp[i][j] = state + prefix[j + 1] - prefix[i]

        return dp[0][n - 1]


# 先区间大小，后区间起点，状态表从对角线向右上角平移
class Solution:
    """
    @param a: An integer array
    @return: An integer
    """
    def stone_game(self, a: List[int]) -> int:
        if not a:
            return 0

        n = len(a)
        prefix = [0] * (n + 1)
        for i in range(len(a)):
            prefix[i + 1] = prefix[i] + a[i]

        # dp = [
        #     [float('inf')] * n
        #     for _ in range(n)
        # ]

        # for i in range(n):
        #     dp[i][i] = 0
        dp = [
            [0] * n
            for _ in range(n)
        ]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                state = float('inf')
                for k in range(i, j):
                    state = min(state, dp[i][k] + dp[k + 1][j])
                dp[i][j] = state + prefix[j + 1] - prefix[i]

        return dp[0][n - 1]
