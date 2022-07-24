# dp-matching
# 谁匹配谁顺序无关，先定义状态、再根据状态转换推导出方程、由方程推导出状态表单元格的依赖方向、初始化
# 一般静态的匹配动态的，简单点

# s行p列
class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def is_match(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [
            [False] * (m + 1)
            for _ in range(n + 1)
        ]

        dp[0][0] = True
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == '*'
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] \
                        or p[j - 1] == '?')
        
        return dp[n][m]


# p行s列
class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def is_match(self, s: str, p: str) -> bool:
        n, m = len(p), len(s)
        dp = [
            [False] * (m + 1)
            for _ in range(n + 1)
        ]

        dp[0][0] = True
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] and p[i - 1] == '*'
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (p[i - 1] == s[j - 1] \
                        or p[i - 1] == '?')
        
        return dp[n][m]


# 滚动数组的两种写法


# memoized search
class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def is_match(self, s: str, p: str) -> bool:
        memo = {}
        
        return self.dfs(s, p, memo)
        
    def dfs(self, s, p, memo):
        if (s, p) in memo:
            return memo[(s, p)]
        
        if not s:
            return not p or self.only_stars(p)
        if not p:
            return not s # must be False
        
        if p[0] == '*':
            res = self.dfs(s, p[1:], memo) or \
                self.dfs(s[1:], p, memo)
        elif p[0] == '?' or p[0] == s[0]:
            res = self.dfs(s[1:], p[1:], memo)
        else:
            res = False
        
        memo[(s, p)] = res
        return res
        
    def only_stars(self, p):
        for v in p:
            if v != '*':
                return False
        
        return True


class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def is_match(self, s: str, p: str) -> bool:
        memo = {}
        
        return self.dfs(s, p, memo)
        
    def dfs(self, s, p, memo):
        if (s, p) in memo:
            return memo[(s, p)]
        
        if not s and not p:
            return True
        if p == '*':
            return True
        if (s and not p) or (p and not s):
            return False
        
        if p[0] == '*':
            res = self.dfs(s, p[1:], memo) or \
                self.dfs(s[1:], p, memo)
        elif p[0] == '?' or p[0] == s[0]:
            res = self.dfs(s[1:], p[1:], memo)
        else:
            res = False
        
        memo[(s, p)] = res
        return res
        

class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def is_match(self, s: str, p: str) -> bool:
        memo = {}
        
        return self.dfs(s, p, memo)
        
    def dfs(self, s, p, memo):
        if not s and not p:
            return True
        if p == '*':
            return True
        if (s and not p) or (p and not s):
            return False
        
        if (s, p) in memo:
            return memo[(s, p)]
        
        res = False
        if p[0] == '?':
            res = self.dfs(s[1:], p[1:], memo)
        elif p[0] == '*':
            for i in range(len(s) + 1):
                if self.dfs(s[i:], p[1:], memo):
                    res = True
                    break
        else:
            if p[0] == s[0]:
                res = self.dfs(s[1:], p[1:], memo)
            else:
                res = False

        memo[(s, p)] = res
        return res



# ----------- 片断研究 ----------------
        elif p[0] == '*':
            # 多路逻辑或，打擂台
            res = False
            for i in range(len(s) + 1):
                res = res or self.dfs(s[i:], p[1:], memo)

        elif p[0] == '*':
            # 短路特判
            res = False
            for i in range(len(s) + 1):
                if self.dfs(s[i:], p[1:], memo):
                    res = True
                    break
