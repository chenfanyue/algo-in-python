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
        if p[0] != '?' and p[0] != '*' and p[0] != s[0]:
            res = False
        elif p[0] != '?' and p[0] != '*' and p[0] == s[0]:
            res = self.dfs(s[1:], p[1:], memo)
        elif p[0] == '?':
            res = self.dfs(s[1:], p[1:], memo)
        elif p[0] == '*':
            for i in range(len(s) + 1):
                if self.dfs(s[i:], p[1:], memo):
                    res = True
                    break
        
        memo[(s, p)] = res
        return res

