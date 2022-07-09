from typing import (
    Set,
)

# memoized search, 求方案总数，不是具体方案
class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def word_break3(self, s: str, words_set: Set[str]) -> int:
        if not s or not words_set:
            return 0
        
        s = s.lower()
        longest = 0
        words = set()
        for word in words_set:
            lw = len(word)
            longest = longest if lw <= longest else lw
            words.add(word.lower())
        
        memo = {}
        start = 0

        return self.dfs(s, start, longest, words, memo)
    
    def dfs(self, s, start, longest, words, memo):
        n = len(s)
        if start == n:
            return 1
        
        if start in memo:
            return memo[start]
        
        res = 0
        for i in range(start, n):
            if i == start + longest:
                break
            if s[start: i+1] not in words:
                continue
            res += self.dfs(s, i + 1, longest, words, memo)
        
        memo[start] = res
        return res


