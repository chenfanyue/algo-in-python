import heapq

class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nth_ugly_number(self, n: int) -> int:
        # write your code here
        h = []
        heapq.heappush(h, 1)
        seen = set([1])
        factors = [2, 3, 5]

        for _ in range(n - 1):
            cur = heapq.heappop(h)
            for f in factors:
                new = cur * f
                if new not in seen:
                    heapq.heappush(h, new)
                    seen.add(new)
        
        return h[0]


class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nth_ugly_number(self, n: int) -> int:
        # write your code here
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            v2 = dp[p2] * 2
            v3 = dp[p3] * 3
            v5 = dp[p5] * 5
            min_v = min(v2, v3, v5)
            dp[i] = min_v

            if min_v == v2:
                p2 += 1
            if min_v == v3:
                p3 += 1
            if min_v == v5:
                p5 += 1
        
        return dp[n]
    

# deprecated, 枚举的效率非常低，未解决大数值无效计算的问题
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nth_ugly_number(self, n: int) -> int:
        # write your code here
        cnt = 0
        res = 0
        i = 1
        is_set = set()
        while cnt < n:
            if self.is_ugly(i, is_set):
                is_set.add(i)
                res = i
                cnt += 1
            i += 1
        
        return res

    def is_ugly(self, val, is_set):
        while val % 2 == 0:
            val //= 2
            if val in is_set:
                return True
        while val % 3 == 0:
            val //= 3
            if val in is_set:
                return True
        while val % 5 == 0:
            val //= 5
            if val in is_set:
                return True
        
        if val == 1:
            return True
        
        return False
