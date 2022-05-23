class Solution:
    """
    @param n: the given number
    @return:  the double factorial of the number
    """
    def double_factorial(self, n: int) -> int:
        # Write your code here
        if n <= 2:
            return n
        return n * self.double_factorial(n - 2)


尾递归，执行速度很快
class Solution:
    """
    @param n: the given number
    @return:  the double factorial of the number
    """
    def double_factorial(self, n: int) -> int:
        # Write your code here
        return self.double_factorial_helper(n)
    
    def double_factorial_helper(self, n, res = 1):
        if n <= 2:
            return res * n
        res *= n
        return self.double_factorial_helper(n - 2, res)


class Solution:
    """
    @param n: the given number
    @return:  the double factorial of the number
    """
    def double_factorial(self, n: int) -> int:
        # Write your code here
        res = 1
        while n >= 2:
            res *= n
            n -= 2
        return res


class Solution:
    """
    @param n: the given number
    @return:  the double factorial of the number
    """
    def double_factorial(self, n: int) -> int:
        # Write your code here
        res = 1
        for i in range(n, 0, -2):
            res *= i
        return res
