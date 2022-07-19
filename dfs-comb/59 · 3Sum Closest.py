from typing import (
    List,
)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def three_sum_closest(self, numbers: List[int], target: int) -> int:
        if not numbers or len(numbers) < 3:
            return 0

        numbers.sort()
        visited = set()
        res = [float('inf'), 0] # distance, cnt
        path = []
        cnt = 0

        self.dfs(numbers, 0, cnt, target, visited, path, res)

        return res[1]

    def dfs(self, numbers, start, cnt, target, visited, path, res):
        if len(path) == 3:
            if (distance := abs(cnt - target)) < res[0]:
                res[0], res[1] = distance, cnt
            return
        if start == len(numbers):
            return

        for i in range(start, len(numbers)):
            if i > 0 and i - 1 not in visited and numbers[i] == numbers[i-1]:
                continue
            val = numbers[i]
            path.append(val)
            visited.add(i)
            self.dfs(numbers, i + 1, cnt + val, target, visited, path, res)
            visited.discard(i)
            path.pop()
