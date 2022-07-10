class Solution:
    """
    @param a: the greater number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        
        return self.gcd(b, a % b)


class Solution:
    """
    @param a: the greater number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        
        return a
