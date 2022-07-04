from typing import (
    List,
)

# dp, 01 backpack, i个的子集装背包j能否刚好装满
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        n = len(a)
        dp = [
            [False] * (m + 1)
            for _ in range(n + 1)
        ]

        dp[0][0] = True
        
        for i in range(1, n + 1):
            for j in range(m + 1):
                if j >= a[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - a[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        for j in range(m, -1, -1):
            if dp[n][j]:
                return j


# the best solution
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        n = len(a)
        dped = [False] * (m + 1) # i=0
        dped[0] = True
        dp = [False] * (m + 1) # i=1
        
        for i in range(1, n + 1):
            for j in range(m + 1):
                if j >= a[i-1]:
                    dp[j] = dped[j] or dped[j - a[i-1]]
                else:
                    dp[j] = dped[j]
            dp, dped = dped, dp
        
        for j in range(m, -1, -1):
            if dped[j]:
                return j



# -------------------------------------

# dp, 01 backpack, i个的子集装背包j最多能装多少
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        n = len(a)
        dp = [
            [0] * (m + 1)
            for _ in range(n + 1)
        ]

        # for j in range(m + 1):
        #     dp[0][j] = 0
        
        for i in range(1, n + 1):
            for j in range(m + 1):
                if j >= a[i-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j - a[i-1]] + a[i-1])
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][m]


# dped, dp rolled down
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        n = len(a)
        dped = [0] * (m + 1) # i=0
        dp = [0] * (m + 1) # i=1
        
        for i in range(1, n + 1):
            for j in range(m + 1):
                if j >= a[i-1]:
                    dp[j] = max(dped[j], dped[j - a[i-1]] + a[i-1])
                else:
                    dp[j] = dped[j]
            dp, dped = dped, dp
        
        return dped[m]



