from typing import (
    List,
)

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        n, m = len(matrix), len(matrix[0])

        line = self.find_last_less_than(matrix, n, target)
        if line == -1:
            return False

        left, right = 0, m - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if target < matrix[line][mid]:
                right = mid
            else:
                left = mid
        if matrix[line][left] == target:
            return True
        if matrix[line][right] == target:
            return True
        return False
    
    def find_last_less_than(self, matrix, n, target):
        left, right = 0, n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if target < matrix[mid][0]:
                right = mid
            else:
                left = mid
        if matrix[right][0] <= target:
            return right
        if matrix[left][0] <= target:
            return left
        return -1


class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        n, m = len(matrix), len(matrix[0])
        left, right = 0, n * m - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if target < self.get(matrix, mid, m):
                right = mid
            else:
                left = mid
        if self.get(matrix, left, m) == target:
            return True
        if self.get(matrix, right, m) == target:
            return True
        return False
    
    def get(self, matrix, idx, m):
        x = idx // m
        y = idx % m
        return matrix[x][y]
