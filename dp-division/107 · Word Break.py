from typing import (
    Set,
)

class Solution:
    """
    @param s: A string
    @param word_set: A dictionary of words dict
    @return: A boolean
    """
    def word_break(self, s: str, word_set: Set[str]) -> bool:
        longest = 0
        for v in word_set:
            len_word = len(v)
            if len_word > longest:
                longest = len_word
        
        n = len(s)
        dp = [False] * (n + 1)

        dp[0] = True

        for i in range(1, n + 1):
            for j in range(max(0, i - longest), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]
