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
        
        if (s, p) in memo:
            return memo[(s, p)]

        res = False
        if len(p) >= 2 and p[1] == '*':
            if p[0] == '.':
                for i in range(len(s) + 1):
                    if self.repeated(s[0:i]):
                        # res = res or self.dfs(s[i:], p[2:], memo)
                        res = self.dfs(s[i:], p[2:], memo)
                        if res:
                            break
            else:
                for i in range(len(s) + 1):
                    if self.repeated_char(s[0:i], p[0]):
                        res = self.dfs(s[i:], p[2:], memo)
                        if res:
                            break
        
        elif p[0] == '.':
            res = self.dfs(s[1:], p[1:], memo)
        # elif p[0] != '.':
        #     if s[0] != p[0]:
        #         res = False
        #     else:
        #         res = self.dfs(s[1:], p[1:], memo)
        elif p[0] != '.' and s[0] == p[0]:
            res = self.dfs(s[1:], p[1:], memo)

        memo[(s, p)] = res
        return res

    def repeated(self, s):
        if not s or len(s) == 1:
            return True
        
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                return False
        
        return True

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
