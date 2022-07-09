from typing import (
    List,
    Set,
)

# enumerate dictionary, time limit exceeded
class Solution:
    """
    @param s: A string
    @param word_dict: A set of words.
    @return: All possible sentences.
             we will sort your return value in output
    """
    def word_break(self, s: str, word_dict: Set[str]) -> List[str]:
        if not s or not word_dict:
            return []
        
        word_dict = sorted(word_dict, key=lambda i: len(i))
        
        path = []
        res = []
        cnt = 0

        self.dfs(word_dict, s, path, cnt, res)

        return res
    
    def dfs(self, word_dict, s, path, cnt, res):
        n = len(s)
        if cnt == n:
            res.append(' '.join(path))
            return
        
        for i in range(len(word_dict)):
            word_len = len(word_dict[i])
            if cnt + word_len > n:
                break
            if s[cnt : cnt + word_len] != word_dict[i]:
                continue
            path.append(word_dict[i])
            self.dfs(word_dict, s, path, cnt + word_len, res)
            path.pop()


# divide string, time limit exceeded
class Solution:
    """
    @param s: A string
    @param word_dict: A set of words.
    @return: All possible sentences.
             we will sort your return value in output
    """
    def word_break(self, s: str, word_dict: Set[str]) -> List[str]:
        if not s or not word_dict:
            return []
        
        longest = 0
        for word in word_dict:
            lw = len(word)
            longest = longest if lw <= longest else lw
        
        path, res = [], []
        start = 0
        memo = {}

        self.dfs(s, start, path, res, longest, word_dict, memo)

        return res
    
    def dfs(self, s, start, path, res, longest, word_dict, memo):
        n = len(s)
        if start == n:
            res.append(' '.join(path))
            return
        
        for i in range(start, n):
            if i == start + longest:
                break
            if s[start: i+1] not in word_dict:
                continue
            path.append(s[start: i+1])
            self.dfs(s, i + 1, path, res, longest, word_dict, memo)
            path.pop()


