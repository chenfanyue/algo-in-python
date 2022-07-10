class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fast_power(self, a: int, b: int, n: int) -> int:
        if n == 0:
            return 1 % b
        
        left = self.fast_power(a, b, n // 2)
        right = left if n % 2 == 0 else left * a % b
        
        return left * right % b


class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fast_power(self, a: int, b: int, n: int) -> int:
        if n == 0:
            return 1 % b
        
        x = self.fast_power(a, b, n // 2)
        res = x * x % b

        if n % 2 == 1:
            res = res * a % b
        
        return res


class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fast_power(self, a: int, b: int, n: int) -> int:
        if b == 1:
            return 0
        
        res = 1

        while n:
            if n % 2:
                res = res * a % b
            a = a % b * a % b
            n = n >> 1
        
        return res



