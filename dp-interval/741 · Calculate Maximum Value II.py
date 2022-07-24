class Solution:
    """
    @param str: a string of numbers
    @return: the maximum value
    """
    def max_value(self, s: str) -> int:
        if not s:
            return 0

        a = [int(ch) for ch in s]
        n = len(a)
        dp = [
            [float('-inf')] * n
            for _ in range(n)
        ]

        for i in range(n):
            dp[i][i] = a[i]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                for k in range(i, j):
                    dp[i][j] = max(
                        dp[i][j],
                        max(dp[i][k] + dp[k + 1][j], dp[i][k] * dp[k + 1][j])
                    )
        
        return dp[0][n - 1]


class Solution:
    """
    @param str: a string of numbers
    @return: the maximum value
    """
    def max_value(self, s: str) -> int:
        if not s:
            return 0

        a = [int(ch) for ch in s]
        n = len(a)
        dp = [
            [float('-inf')] * n
            for _ in range(n)
        ]

        for i in range(n):
            dp[i][i] = a[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    dp[i][j] = max(
                        dp[i][j],
                        max(dp[i][k] + dp[k + 1][j], dp[i][k] * dp[k + 1][j])
                    )
        
        return dp[0][n - 1]

