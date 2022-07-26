# 滚动数组
class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def num_decodings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [1, 0, 0]
        dp[1] = 1 if 1 <= int(s[0]) <= 9 else 0

        for i in range(2, n + 1):
            idx = i % 3
            dp[idx] = 0
            if self.valid(s[i - 1]):
                dp[idx] += dp[(i - 1) % 3]
            if self.valid(s[i - 2: i]):
                dp[idx] += dp[(i - 2) % 3]
        
        return dp[n % 3]

    def valid(self, s):
        if len(s) == 1:
            return 1 <= int(s) <= 9
        if len(s) == 2:
            return 10 <= int(s) <= 26


# 可行性系数
class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def num_decodings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [1, 0, 0]
        dp[1] = 1 if 1 <= int(s[0]) <= 9 else 0

        for i in range(2, n + 1):
            dp[i % 3] = self.valid(s[i - 1]) * dp[(i - 1) % 3] + \
                self.valid(s[i - 2: i]) * dp[(i - 2) % 3]
        
        return dp[n % 3]

    def valid(self, s):
        if len(s) == 1 and 1 <= int(s) <= 9:
            return 1
        if len(s) == 2 and 10 <= int(s) <= 26:
            return 1
        return 0



