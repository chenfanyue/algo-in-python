from typing import (
    List,
)

# rough dfs, 没有剪枝
class Solution:
    """
    @param a: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
             we will sort your return value in output
    """
    def k_sum_i_i(self, a: List[int], k: int, target: int) -> List[List[int]]:
        # write your code here
        if not a:
            return []
        
        a.sort()
        comb = []
        res = []
        start = 0

        self.dfs(a, start, comb, k, target, res)

        return res
    
    def dfs(self, a, start, comb, k, target, res):
        if len(comb) == k:
            if sum(comb) == target:
                res.append(list(comb))
            return
        
        for i in range(start, len(a)):
            comb.append(a[i])
            self.dfs(a, i + 1, comb, k, target, res)
            comb.pop()


# dfs + 纵向剪枝
class Solution:
    """
    @param a: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
             we will sort your return value in output
    """
    def k_sum_i_i(self, a: List[int], k: int, target: int) -> List[List[int]]:
        # write your code here
        if not a:
            return []
        
        a.sort()
        comb = []
        res = []
        start = 0

        self.dfs(a, start, comb, k, target, res)

        return res
    
    def dfs(self, a, start, comb, k, target, res):
        comb_sum = sum(comb)
        if len(comb) == k:
            if comb_sum == target:
                res.append(list(comb))
            return
        if comb_sum >= target:
            return
        
        for i in range(start, len(a)):
            # 横向剪枝开销收益基本相抵，没有太大意义，一般只要考虑纵向剪枝
            # if sum(comb) + a[i] > target:
            #     return
            comb.append(a[i])
            self.dfs(a, i + 1, comb, k, target, res)
            comb.pop()



