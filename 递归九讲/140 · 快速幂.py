借助同余定理
分两种降阶：
1.同步降阶 x * y % z = (x % z) * (y % z) % z
2.异步降阶 x * y % z = (x % z * y % z) % z
1 % n -> 0 or 1
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fast_power(self, a: int, b: int, n: int) -> int:
        # write your code here
        if n == 0:
            return 1 % b
        x = self.fast_power(a, b, n // 2)
        y = x if n % 2 == 0 else x * a % b
        return x * y % b
