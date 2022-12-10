class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [None] * numRows
        for i in range(numRows):
            dp[i] = [0] * (i+1)
            for j in range(i+1):
                if j == 0 or j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        for i in range(numRows):
            dp.append([1] * (i+1))
            for j in range(i+1):
                if j == 0 or j == i:
                    continue
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        for i in range(numRows):
            dp.append([1] * (i+1))
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp
