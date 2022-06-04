from typing import (
    List,
)

class Solution:
    """
    @param a: sorted integer array A
    @param b: sorted integer array B
    @return: A new sorted integer array
    """
    def merge_sorted_array(self, a: List[int], b: List[int]) -> List[int]:
        # write your code here
        if not a:
            return b
        if not b:
            return a
        
        return self.merge_helper(a, 0, b, 0, [])

    def merge_helper(self, a, i, b, j, res):
        if i == len(a):
            res.extend(b[j:])
            return res
        if j == len(b):
            res.extend(a[i:])
            return res
        
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
        
        return self.merge_helper(a, i, b, j, res)


class Solution:
    """
    @param a: sorted integer array A
    @param b: sorted integer array B
    @return: A new sorted integer array
    """
    def merge_sorted_array(self, a: List[int], b: List[int]) -> List[int]:
        # write your code here
        if not a:
            return b
        if not b:
            return a
        
        res = []
        self.merge_helper(a, 0, b, 0, res)

        return res

    def merge_helper(self, a, i, b, j, res):
        if i == len(a):
            res.extend(b[j:])
            return
        if j == len(b):
            res.extend(a[i:])
            return
        
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
        
        self.merge_helper(a, i, b, j, res)

        return


class Solution:
    """
    @param a: sorted integer array A
    @param b: sorted integer array B
    @return: A new sorted integer array
    """
    def merge_sorted_array(self, a: List[int], b: List[int]) -> List[int]:
        # write your code here
        if not a:
            return b
        if not b:
            return a
        
        res = []
        i = j = 0
        while True:
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
                if i == len(a):
                    res.extend(b[j:])
                    break
            else:
                res.append(b[j])
                j += 1
                if j == len(b):
                    res.extend(a[i:])
                    break
        
        return res
