分治法
站在问题里面拆解问题
class Solution:
    """
    @param n: an integer
    @return: return an integer
    """
    def reverse_bits(self, n: int) -> int:
        # write your code here
        return self.reverse_bits_helper(n, 32)

    def reverse_bits_helper(self, n: int, bits: int) -> int:
        if bits == 1:
            return n
        last_bit = n & 1
        last_bit_to_first = last_bit << (bits - 1)
        remaining = n >> 1
        return last_bit_to_first + self.reverse_bits_helper(remaining, bits - 1)


尾递归
站在问题外面拆解问题，假设已经完成部分，将问题分为已完成和为完成两部分。逐渐扩大已完成集，缩小未完成集。已完成集作为信使量。
class Solution:
    """
    @param n: an integer
    @return: return an integer
    """
    def reverse_bits(self, n: int) -> int:
        # write your code here
        return self.reverse_bits_helper(n, 32)

    def reverse_bits_helper(self, n: int, bits: int, reversed: int = 0) -> int:
        if bits == 1:
            return reversed + n
        last_bit = n & 1
        reversed += last_bit << (bits - 1)
        remaining = n >> 1
        return self.reverse_bits_helper(remaining, bits - 1, reversed)


步进法，按位印射，迭代
class Solution:
    """
    @param n: an integer
    @return: return an integer
    """
    def reverse_bits(self, n: int) -> int:
        # write your code here
        res = 0
        for i in range(32, 0, -1):
            last_bit = n & 1
            res += last_bit << (i - 1)
            n = n >> 1
        return res


步进法，往左推，迭代
class Solution:
    """
    @param n: an integer
    @return: return an integer
    """
    def reverse_bits(self, n: int) -> int:
        # write your code here
        res = 0
        for i in range(32):
            last_bit = n & 1
            res = (res << 1) + last_bit
            # res = (res << 1) | last_bit
            n = n >> 1
        return res
