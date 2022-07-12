from typing import (
    Set,
)

# 双向bfs，边推进边探索
class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start: str, end: str, word_dict: Set[str]) -> int:
        word_dict.update([start, end])

        forward_q = collections.deque([start])
        forward_visited = set([start])
        backward_q = collections.deque([end])
        backward_visited = set([end])
        
        distance = 0

        while forward_q and backward_q:
            distance += 1
            if self.met(word_dict, forward_q, forward_visited, backward_visited):
                return distance + 1
            
            distance += 1
            if self.met(word_dict, backward_q, backward_visited, forward_visited):
                return distance + 1
        
        return 0

    def met(self, word_dict, q, visited, opposite_visited):
        for _ in range(len(q)):
            cur = q.popleft()
            for neighbor in self.get_neighbors(cur, word_dict):
                if neighbor in visited:
                    continue
                if neighbor in opposite_visited:
                    return True
                q.append(neighbor)
                visited.add(neighbor)
        
        return False

    def get_neighbors(self, word, word_dict):
        alphers = [chr(code) for code in range(ord('a'), ord('z') + 1)]
        neighbors = []

        for i in range(len(word)):
            for ch in alphers:
                if ch == word[i]:
                    continue
                word_new = word[:i] + ch + word[i + 1:]
                if word_new in word_dict:
                    neighbors.append(word_new)
        
        return neighbors


# bi-directional bfs
class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start: str, end: str, word_dict: Set[str]) -> int:
        word_dict.update([start, end])
        graph = self.get_graph(word_dict)

        forward_q = collections.deque([start])
        forward_visited = set([start])
        backward_q = collections.deque([end])
        backward_visited = set([end])
        
        distance = 0

        while forward_q and backward_q:
            distance += 1
            if self.met(graph, forward_q, forward_visited, backward_visited):
                return distance + 1
            
            distance += 1
            if self.met(graph, backward_q, backward_visited, forward_visited):
                return distance + 1
        
        return 0

    def get_graph(self, word_dict):
        graph = dict()
        for word in word_dict:
            graph[word] = self.get_neighbors(word, word_dict)
        
        return graph
    
    def get_neighbors(self, word, word_dict):
        alphers = [chr(code) for code in range(ord('a'), ord('z') + 1)]
        neighbors = []

        for i in range(len(word)):
            for ch in alphers:
                if ch == word[i]:
                    continue
                word_new = word[:i] + ch + word[i + 1:]
                if word_new in word_dict:
                    neighbors.append(word_new)
        
        return neighbors

    def met(self, graph, q, visited, opposite_visited):
        for _ in range(len(q)):
            cur = q.popleft()
            for neighbor in graph[cur]:
                if neighbor in visited:
                    continue
                if neighbor in opposite_visited:
                    return True
                q.append(neighbor)
                visited.add(neighbor)
        
        return False



class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start: str, end: str, word_dict: Set[str]) -> int:
        # write your code here
        word_dict.add(end)
        n = len(start)
        char_dict = [set() for _ in range(n)]
        
        for word in word_dict:
            for i in range(n):
                char_dict[i].add(word[i])
        
        level = 1
        q = collections.deque([start])
        visited = set([start])

        while q:
            level += 1
            window = len(q)
            for _ in range(window):
                cur = q.popleft()
                
                for next_word in self.next_words(cur, char_dict, word_dict, visited):
                    if next_word == end:
                        return level
                    visited.add(next_word)
                    q.append(next_word)
        
        return 0

    def next_words(self, cur, char_dict, word_dict, visited):
        words = []
        for i in range(len(cur)):
            for ch in char_dict[i]:
                next_word = cur[:i] + ch + cur[i+1:]
                if next_word not in word_dict or next_word in visited:
                    continue
                words.append(next_word)
        
        return words


class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start: str, end: str, word_dict: Set[str]) -> int:
        # write your code here
        word_dict.add(end)
        alphers = [chr(code) for code in range(ord('a'), ord('z') + 1)]
        
        level = 1
        q = collections.deque([start])
        visited = set([start])

        while q:
            level += 1
            window = len(q)
            for _ in range(window):
                cur = q.popleft()
                
                for next_word in self.next_words(cur, alphers, word_dict, visited):
                    if next_word == end:
                        return level
                    visited.add(next_word)
                    q.append(next_word)
        
        return 0

    def next_words(self, cur, alphers, word_dict, visited):
        words = []
        for i in range(len(cur)):
            for ch in alphers:
                if ch == cur[i]:
                    continue
                next_word = cur[:i] + ch + cur[i+1:]
                if next_word not in word_dict or next_word in visited:
                    continue
                words.append(next_word)
        
        return words


class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start: str, end: str, word_dict: Set[str]) -> int:
        # write your code here
        word_dict.add(end)
        alphers = [chr(code) for code in range(ord('a'), ord('z') + 1)]
        
        q = collections.deque([start])
        level = {start: 1}

        while q:
            cur = q.popleft()
            
            for next_word in self.next_words(cur, alphers, word_dict, level):
                if next_word == end:
                    return level[next_word]
                q.append(next_word)
        
        return 0

    def next_words(self, cur, alphers, word_dict, level):
        words = []
        for i in range(len(cur)):
            for ch in alphers:
                if ch == cur[i]:
                    continue
                next_word = cur[:i] + ch + cur[i+1:]
                if next_word in word_dict and next_word not in level:
                    level[next_word] = level[cur] + 1
                    words.append(next_word)
        
        return words


class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start: str, end: str, word_dict: Set[str]) -> int:
        # write your code here
        word_dict.add(end)
        alphers = [chr(code) for code in range(ord('a'), ord('z') + 1)]
        
        q = collections.deque([start,'#'])
        visited = set([start])

        level = 1
        while q:
            cur = q.popleft()
            if cur == '#':
                level += 1
                q.append('#')
                continue
            
            for next_word in self.next_words(cur, alphers, word_dict, visited):
                if next_word == end:
                    return level + 1
                visited.add(next_word)
                q.append(next_word)
        
        return 0

    def next_words(self, cur, alphers, word_dict, visited):
        words = []
        for i in range(len(cur)):
            for ch in alphers:
                if ch == cur[i]:
                    continue
                next_word = cur[:i] + ch + cur[i+1:]
                if next_word not in word_dict or next_word in visited:
                    continue
                words.append(next_word)
        
        return words

