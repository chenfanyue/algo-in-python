class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def can_win_bash(self, n: int) -> bool:
        # Write your code here
        return True if n % 4 else False
        # return n % 4 != 0


# 栈深度O(n), 大数发生爆栈
class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def can_win_bash(self, n: int) -> bool:
        # Write your code here
        return self.memo_search(n, {})
    
    def memo_search(self, n, memo):
        if n <= 3:
            return True
        
        if n in memo:
            return memo[n]
        
        for i in range(1, 4):
            if not self.memo_search(n - i, memo):
                memo[n] = True
                return True
        
        memo[n] = False
        return False


# 伪dp
class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def can_win_bash(self, n: int) -> bool:
        # Write your code here
        dp = [False] * n

        for i in range(min(3, n)):
            dp[i] = True
        
        for i in range(3, n):
            if dp[i - 3] and dp[i - 2] and dp[i - 1]:
                dp[i] = False
            else:
                dp[i] = True
        
        return dp[n - 1]



