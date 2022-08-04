from typing import (
    Set,
)

# bfs
class Solution:
    """
    @param s: a string
    @param dict: a set of n substrings
    @return: the minimum length
    """
    def min_length(self, s: str, d: Set[str]) -> int:
        res = len(s)
        q = collections.deque([s])
        visited = set([s])

        while q:
            s = q.popleft()
            for sub in d:
                if sub == s:
                    return 0
                idx = s.find(sub)
                while idx != -1:
                    new_s = s[:idx] + s[idx + len(sub):]
                    if new_s not in visited:
                        res = min(res, len(new_s))
                        visited.add(new_s)
                        q.append(new_s)
                    idx = s.find(sub, idx + 1)
        
        return res


# dfs
class Solution:
    """
    @param s: a string
    @param dict: a set of n substrings
    @return: the minimum length
    """
    def min_length(self, s: str, d: Set[str]) -> int:
        memo = {}

        return self.dfs(s, d, memo)

    def dfs(self, s, d, memo):
        if not s:
            return 0
        if s in memo:
            return memo[s]

        res = float('inf')
        for sub in d:
            if sub == s:
                res = 0
                break
            idx = s.find(sub)
            while idx != -1:
                new_s = s[:idx] + s[idx + len(sub):]
                res = min(res, self.dfs(new_s, d, memo))
                idx = s.find(sub, idx + 1)
        
        if res == float('inf'):
            res = len(s)
        
        memo[s] = res
        return res
