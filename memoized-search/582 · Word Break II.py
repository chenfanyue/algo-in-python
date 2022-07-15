from typing import (
    List,
    Set,
)

# divide string, 划分型dfs，可求方案总数或具体方案，要点是返回方案要压为一维才好处理
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
        
        memo = {}

        return self.dfs(s, 0, longest, word_dict, memo)

    def dfs(self, s, start, longest, word_dict, memo):
        n = len(s)
        if start == n:
            return ['']
        
        if start in memo:
            return memo[start]
        
        res = []
        for i in range(start, n):
            if i == start + longest:
                break
            left = s[start: i+1]
            if left not in word_dict:
                continue

            right = self.dfs(s, i + 1, longest, word_dict, memo)
            if not right:
                continue

            if right == ['']:
                res.append(left)
                break
            for each in right:
                res.append(left + ' ' + each)
        
        memo[start] = res
        return res


# enumerate dictionary, time limit exceeded, not recommended
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


