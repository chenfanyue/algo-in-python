class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def is_match(self, s: str, p: str) -> bool:
        memo = {}

        return self.dfs(s, p, memo)

    def dfs(self, s, p, memo):
        if (s, p) in memo:
            return memo[(s, p)]

        if not s and not p:
            return True
        if p == '.*':
            return True
        if not p and s:
            return False
        if not s and p:
            if len(p) % 2 == 0 and self.oven_star(p):
                return True
            return False
        
        if len(p) >= 2 and p[1] == '*':
            if p[0] == '.':
                # res = False
                # for i in range(len(s) + 1):
                #     if self.dfs(s[i:], p[2:], memo):
                #         res = True
                #         break
                res = self.dfs(s, p[2:], memo) or \
                    self.dfs(s[1:], p, memo)
            else:
                res = False
                for i in range(len(s) + 1):
                    if self.repeated_char(s[0:i], p[0]) and \
                        self.dfs(s[i:], p[2:], memo):
                        res = True
                        break
        elif p[0] == '.' or p[0] == s[0]:
            res = self.dfs(s[1:], p[1:], memo)
        else: 
            res = False

        memo[(s, p)] = res
        return res

    def repeated_char(self, s, ch):
        if not s:
            return True
        
        for i in range(len(s)):
            if s[i] != ch:
                return False
        
        return True

    def oven_star(self, p):
        for i in range(1, len(p), 2):
            if p[i] != '*':
                return False
        
        return True


class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def is_match(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = True
        for j in range(1, m + 1):
            if j % 2 == 0:
                dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    if p[j - 2] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2] or (s[i - 1] == p[j - 2] and dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == '.' or p[j - 1] == s[i - 1])
        
        return dp[n][m]

