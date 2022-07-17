from typing import (
    List,
)

# 按字典序该排列在全部的排列里排在第几个
class Solution:
    """
    @param a: An array of integers
    @return: A long integer
    """
    def permutation_index(self, a: List[int]) -> int:
        res = 0
        factorial = 1

        for i in range(len(a) - 2, -1, -1):
            smaller = 0
            for j in range(i + 1, len(a)):
                if a[j] < a[i]:
                    smaller += 1
            
            res += smaller * factorial
            factorial *= len(a) - i

        return res + 1
