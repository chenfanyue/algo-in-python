from typing import (
    List,
)

# 排除法
class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        x, y = n - 1, 0
        cnt = 0
        while x > -1 and y < m:
            if matrix[x][y] == target:
                cnt += 1
                x -= 1
                y += 1
            elif matrix[x][y] < target:
                y += 1
            else:
                x -= 1
        
        return cnt
