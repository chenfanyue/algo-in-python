from typing import (
    List,
)
from collections import defaultdict

class Solution:
    """
    @param a: list of quantities of other rabbits of same color
    @return: the minimum number of rabbits that could be in the forest.
    """
    def num_rabbits(self, a: List[int]) -> int:
        if not a:
            return 0

        d = defaultdict(int)
        for v in a:
            d[v + 1] += 1

        res = 0
        for i, v in d.items():
            margin = 0 if v % i == 0 else 1
            res += i * (v // i + margin) # math.ceil(v / i)

        return res
