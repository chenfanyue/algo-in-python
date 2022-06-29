from typing import (
    List,
)

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
             we will sort your return value in output
    """
    def word_search_i_i(self, board: List[List[str]], words: List[str]) -> List[str]:
        # write your code here
        if not board or not words:
            return []
        
        self.DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        board = board
        words_set = set(words)
        res = []

        longest = 0
        for word in words:
            longest = max(longest, len(word))
        
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[: i + 1])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, [board[i][j]], {(i, j)}, prefix_set, words_set, res, longest)
        
        return res
    
    def dfs(self, board, i, j, path, visited, prefix_set, words_set, res, longest):
        word = ''.join(path)
        if word not in prefix_set:
            return
        if word in words_set:
            res.append(word)
            words_set.remove(word)
        if len(path) == longest:
            return

        for delta_x, delta_y in self.DIRECTIONS:
            x = i + delta_x
            y = j + delta_y
            if not self.in_boundry(board, x, y) or (x, y) in visited:
                continue
            visited.add((x, y))
            path.append(board[x][y])
            self.dfs(board, x, y, path, visited, prefix_set, words_set, res, longest)
            visited.remove((x, y))
            path.pop()
    
    def in_boundry(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
