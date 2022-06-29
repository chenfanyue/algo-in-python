from typing import (
    List,
)

# divide and conquer, memorization
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimum_total(self, triangle: List[List[int]]) -> int:
        # write your code here
        return self.dfs(triangle, 0, 0, dict())

    def dfs(self, triangle, x, y, memo):
        if x + 1 == len(triangle):
            return triangle[x][y]
        
        if (x, y) in memo:
            return memo[(x, y)]
        
        left = self.dfs(triangle, x + 1, y, memo)
        right = self.dfs(triangle, x + 1, y + 1, memo)

        memo[(x, y)] = min(left, right) + triangle[x][y]
        return memo[(x, y)]


# dfs, 已知状态量 + 即将访问的一层
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimum_total(self, triangle: List[List[int]]) -> int:
        # write your code here
        cnt = 0
        res = []
        self.dfs(triangle, 0, 0, cnt, res)

        return min(res)

    def dfs(self, triangle, x, y, cnt, res):
        if x == len(triangle):
            res.append(cnt)
            return
        
        self.dfs(triangle, x + 1, y, cnt + triangle[x][y], res)
        self.dfs(triangle, x + 1, y + 1, cnt + triangle[x][y], res)


# not recommended, 一般不要这么写
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimum_total(self, triangle: List[List[int]]) -> int:
        # write your code here
        cnt = triangle[0][0]
        res = []
        self.dfs(triangle, 0, 0, cnt, res)

        return min(res)

    def dfs(self, triangle, x, y, cnt, res):
        if x + 1 == len(triangle):
            res.append(cnt)
            return
        
        self.dfs(triangle, x + 1, y, cnt + triangle[x + 1][y], res)
        self.dfs(triangle, x + 1, y + 1, cnt + triangle[x + 1][y + 1], res)



