class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverse_integer(self, n: int) -> int:
        # write your code here
        if n == 0:
            return 0

        positive = True
        if n < 0:
            positive = False
            n = abs(n)

        res = 0
        while n > 0:
            res = res * 10 + n % 10
            n //= 10

        if positive:
            if res <= (1 << 31) - 1:
                return res
            return 0
        else:
            if -res < -(1 << 31):
                return 0
            return -res


class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverse_integer(self, n: int) -> int:
        # write your code here
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        res = 0
        while n != 0:
            if res < INT_MIN // 10 + 1 or res > INT_MAX // 10:
                return 0
            digit = n % 10
            if n < 0 and digit > 0:
                digit -= 10
            n = (n - digit) // 10
            res = res * 10 + digit
        
        return res


class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverse_integer(self, n: int) -> int:
        # write your code here
        INT_MIN, INT_MAX = -2**31 // 10 + 1, (2**31 - 1) // 10
        res = 0
        while n != 0:
            if res < INT_MIN or res > INT_MAX:
                return 0
            digit = n % 10
            if n < 0 and digit > 0:
                digit -= 10
            res = res * 10 + digit
            n = (n - digit) // 10
        
        return res

