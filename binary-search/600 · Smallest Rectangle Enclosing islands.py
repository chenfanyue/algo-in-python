from typing import (
    List,
)

# 二分法，在定义函数里调用抽象函数
class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def min_area(self, image: List[List[str]], x: int, y: int) -> int:
        if not image or not image[0]:
            return 0
        
        n, m = len(image), len(image[0])
        left = self.get_first_existed(image, 0, y, self.check_col)
        right = self.get_last_existed(image, y, m - 1, self.check_col)
        top = self.get_first_existed(image, 0, x, self.check_row)
        bottom = self.get_last_existed(image, x, n - 1, self.check_row)

        return (right - left + 1) * (bottom - top + 1)
    
    def get_first_existed(self, image, left, right, check_func):
        while left + 1 < right:
            mid = (left + right) // 2
            if check_func(image, mid):
                right = mid
            else:
                left = mid
        if check_func(image, left):
            return left
        return right

    def get_last_existed(self, image, left, right, check_func):
        while left + 1 < right:
            mid = (left + right) // 2
            if check_func(image, mid):
                left = mid
            else:
                right = mid
        if check_func(image, right):
            return right
        return left
    
    def check_col(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return True
        return False

    def check_row(self, image, row):
        for j in range(len(image[0])):
            if image[row][j] == '1':
                return True
        return False




