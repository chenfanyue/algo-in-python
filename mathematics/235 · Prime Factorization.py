from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @return: an integer array
    """
    def prime_factorization(self, n: int) -> List[int]:
        res = []
        up = int(math.sqrt(n))

        k = 2
        while k <= up and n > 1:
            while n % k == 0:
                res.append(k)
                n //= k
            k += 1
        
        if n > 1:
            res.append(n)
        
        return res
