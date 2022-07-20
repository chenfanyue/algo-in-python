from typing import (
    List,
)

# 一拖二，三指针, n^2
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
        res, distance = float('inf'), float('inf')

        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left, right = i + 1, len(numbers) - 1
            while left < right:
                total = numbers[i] + numbers[left] + numbers[right]
                if total == target:
                    return total
                
                if (d := abs(total - target)) < distance:
                    res, distance = total, d
                
                if total < target:
                    left += 1
                    while numbers[left] == numbers[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while numbers[right] == numbers[right + 1]:
                        right -= 1
        
        return res


# comb-like dfs, n^3
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
