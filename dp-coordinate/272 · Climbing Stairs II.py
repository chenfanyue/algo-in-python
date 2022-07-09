# 滑动窗口
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climb_stairs2(self, n: int) -> int:
        if n <= 1:
            return 1
        if n == 2:
            return 2
        
        a, b, c = 1, 1, 2

        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        
        return c


# memoized search
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climb_stairs2(self, n: int) -> int:
        memo = {}

        return self.dfs(0, n, memo)
    
    def dfs(self, begin, n, memo):
        if begin == n:
            return 1
        
        if begin in memo:
            return memo[begin]
        
        res = 0
        for i in range(begin + 1, n + 1):
            if i - begin > 3:
                break
            res += self.dfs(i, n, memo)
        
        memo[begin] = res
        return res


# memoized search
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climb_stairs2(self, n: int) -> int:
        if n == 0:
            return 1
        
        memo = {}

        return self.dfs(n, memo)
    
    def dfs(self, n, memo):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        
        if n in memo:
            return memo[n]
        
        res = self.dfs(n - 1, memo) + \
                self.dfs(n - 2, memo) + \
                self.dfs(n - 3, memo)
        
        memo[n] = res
        return res


# memoized search
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climb_stairs2(self, n: int) -> int:
        memo = {}

        return self.dfs(n, memo)
    
    def dfs(self, n, memo):
        if n == 0:
            return 1
        
        if n in memo:
            return memo[n]
        
        res = 0
        for i in range(1, 4):
            remaining = n - i
            if remaining < 0:
                break
            res += self.dfs(remaining, memo)
        
        memo[n] = res
        return res


# dp
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climb_stairs2(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        
        return dp[n]


# not recommended, 滚动数组
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climb_stairs2(self, n: int) -> int:
        if n <= 1:
            return 1
        if n == 2:
            return 2
        
        dp = [1, 1, 2]

        for i in range(3, n + 1):
            dp[i % 3] = dp[0] + dp[1] + dp[2]
        
        return dp[n % 3]


# not recommended, kind of awful
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climb_stairs2(self, n: int) -> int:
        if n <= 1:
            return 1
        if n == 2:
            return 2
        
        dp = [1, 1, 2]

        i = 0
        for _ in range(3, n + 1):
            dp[i] = dp[0] + dp[1] + dp[2]
            i += 1
            if i == 3:
                i = 0
        
        return dp[(i + 2) % 3]
