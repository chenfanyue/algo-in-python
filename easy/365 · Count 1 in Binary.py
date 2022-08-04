class Solution:
    """
    @param n: An integer
    @return: An integer, the number of ones in n
    """
    def count_ones(self, n: int) -> int:
        res = 0

        for i in range(32):
            if n & (1 << i):
            	res += 1

        return res


# below just suitable for non-negative
        while n:
            n = n & (n - 1)
            res += 1

        while n:
            res += n & 1
            n >>= 1

