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
        self.board = board
        self.words_set = set(words)
        self.res = []

        self.longest = 0
        for word in words:
            self.longest = max(self.longest, len(word))
        self.prefix = [set()] * self.longest
        
        for word in words:
            for k in range(len(word)):
                self.prefix[k].add(word[: k + 1])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.prefix[0]:
                    self.helper(i, j, 0, board[i][j], {(i, j)})
        
        return self.res
    
    def helper(self, i, j, k, route, visited):
        if route not in self.prefix[k]:
            return
        if route in self.words_set:
            self.res.append(route)
            self.words_set.remove(route)
        
        if self.longest - 1 == k:
            return

        for delta_x, delta_y in self.DIRECTIONS:
            x = i + delta_x
            y = j + delta_y
            if not self.in_boundry(x, y) or (x, y) in visited:
                continue
            # route += self.board[x][y] # ignored instead use func-call-frame
            visited.add((x, y))
            self.helper(x, y, k + 1, route + self.board[x][y], visited)
            visited.remove((x, y))
    
    def in_boundry(self, x, y):
        return 0 <= x < len(self.board) and 0 <= y < len(self.board[x])


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
             we will sort your return value in output
    """
    def word_search_i_i(self, board: List[List[str]], words: List[str]) -> List[str]:
        # write your code here
        self.DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.board = board
        self.words_set = set(words)
        self.prefix = set()
        captains = set()
        self.res = set() # in order to avoid duplication
        
        for word in words:
            for i in range(len(word)):
                captains.add(word[0])
                self.prefix.add(word[: i + 1])
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in captains:
                    self.helper(i, j, board[i][j], {(i, j)})
        
        return list(self.res)
    
    def helper(self, i, j, route, visited):
        if route not in self.prefix:
            return
        if route in self.words_set:
            self.res.add(route)

        for delta_x, delta_y in self.DIRECTIONS:
            x = i + delta_x
            y = j + delta_y
            if not self.in_boundry(x, y) or (x, y) in visited:
                continue
            # route += self.board[x][y] # ignored instead use func-call-frame
            visited.add((x, y))
            self.helper(x, y, route + self.board[x][y], visited)
            visited.remove((x, y))
    
    def in_boundry(self, x, y):
        return 0 <= x < len(self.board) and 0 <= y < len(self.board[x])


# awful, not recommended
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
             we will sort your return value in output
    """
    def word_search_i_i(self, board: List[List[str]], words: List[str]) -> List[str]:
        # write your code here
        self.DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.board = board
        self.words_set = set(words)
        self.prefix = set()
        captains = set()
        self.route = []
        self.visited = set()
        self.res = set() # in order to avoid duplication
        
        for word in words:
            for i in range(len(word)):
                captains.add(word[0])
                self.prefix.add(word[: i + 1])
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in captains:
                    self.route.append(board[i][j])
                    self.visited.add((i, j))
                    self.helper(i, j)
                    self.route.pop()
                    self.visited.remove((i, j))
        
        return list(self.res)
    
    def helper(self, i, j):
        word = ''.join(self.route)
        if word not in self.prefix:
            return
        if word in self.words_set:
            self.res.add(word)

        for delta_x, delta_y in self.DIRECTIONS:
            x = i + delta_x
            y = j + delta_y
            if not self.in_boundry(x, y) or (x, y) in self.visited:
                continue

            self.route.append(self.board[x][y])
            self.visited.add((x, y))
            self.helper(x, y)
            self.route.pop()
            self.visited.remove((x, y))
    
    def in_boundry(self, x, y):
        return 0 <= x < len(self.board) and 0 <= y < len(self.board[x])


# not recommended
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
             we will sort your return value in output
    """
    def word_search_i_i(self, board: List[List[str]], words: List[str]) -> List[str]:
        # write your code here
        self.DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.board = board
        self.words_set = set(words)
        self.prefix = set()
        # captains = set()
        self.res = set() # in order to avoid duplication
        
        for word in words:
            for i in range(len(word)):
                # captains.add(word[0])
                self.prefix.add(word[: i + 1])
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                # if board[i][j] in captains:
                self.helper(i, j, board[i][j], {(i, j)})
        
        return list(self.res)
    
    def helper(self, i, j, route, visited):
        if route not in self.prefix:
            return
        if route in self.words_set:
            self.res.add(route)

        for delta_x, delta_y in self.DIRECTIONS:
            x = i + delta_x
            y = j + delta_y
            if not self.in_boundry(x, y) or (x, y) in visited:
                continue
            # route += self.board[x][y] # ignored instead use func-call-frame
            visited.add((x, y))
            self.helper(x, y, route + self.board[x][y], visited)
            visited.remove((x, y))
    
    def in_boundry(self, x, y):
        return 0 <= x < len(self.board) and 0 <= y < len(self.board[x])


# awful, not recommended
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if board is None or len(board) == 0:
            return []
        
        # pre-process
        # 预处理
        word_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
        
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(
                    board,
                    i,
                    j,
                    board[i][j],
                    word_set,
                    prefix_set,
                    set([(i, j)]),
                    result,
                )
                
        return list(result)
        
    def search(self, board, x, y, word, word_set, prefix_set, visited, result):
        if word not in prefix_set:
            return
        
        if word in word_set:
            result.add(word)
        
        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y
            
            if not self.inside(board, x_, y_):
                continue
            if (x_, y_) in visited:
                continue
            
            visited.add((x_, y_))
            self.search(
                board,
                x_,
                y_,
                word + board[x_][y_],
                word_set,
                prefix_set,
                visited,
                result,
            )
            visited.remove((x_, y_))
            
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])


