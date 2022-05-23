class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n: int) -> int:
        # write your code here
        if 1 == n:
            return 0
        if 2 == n:
            return 1
        
        former = 0
        latter = 1
        for i in range(3, n+1):
            former, latter = latter, former + latter
        return latter


递推法
class Solution:
    def fibonacci(self, n):
        fib = [0, 0, 1]
        for i in range(3, n + 1, 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]


动态规划的滚动数组思想
class Solution:
    def fibonacci(self, n):
        fib = [0, 1]
        for i in range(2, n):
            fib[i % 2] = fib[0] + fib[1]
        return fib[(n - 1) % 2]


记忆化搜索——以空间换时间的优化算法
将计算出的结果存储下来，在计算到指定值的时候，先判断这个值是否已经计算过，若没有，才进行计算，否则读取已经存储下来的值。这样就把一个指数级复杂度变成了线性复杂度，代价是空间复杂度从常数级上升至线性级。时间复杂度为O(n)，空间复杂度为O(n)。

class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n: int) -> int:
        # write your code here
        arr = [-1] * (n + 1)
        return self.x(n, arr)

    def x(self, n, arr: List[int]) -> int:
        if arr[n] > -1:
            return arr[n]
        if n <= 2:
            arr[n] = n - 1
            return arr[n]

        arr[n] = self.x(n - 2, arr) + self.x(n - 1, arr)
        return arr[n]


class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n: int) -> int:
        # write your code here
        if n <= 2:
            return n - 1
        
        arr = [-1] * (n + 1)
        arr[1] = 0
        arr[2] = 1
        return self.x(n, arr)

    def x(self, n, arr: List[int]) -> int:
        if arr[n] > -1:
            return arr[n]
        arr[n] = self.x(n - 2, arr) + self.x(n - 1, arr)
        return arr[n]
