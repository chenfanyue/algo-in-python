# 描述
# 给出一个非负整数数组，你最初定位在数组的第一个位置。
# 数组中的每个元素代表你在那个位置可以跳跃的最大长度。
# 判断你是否能到达数组的最后一个位置。
# 数组A的长度不超过5000，每个元素的大小不超过5000

from typing import (
    List,
)

# solution 1-a
# T = O(n), algo: energy-driven move, while, joy run game
class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    def can_jump(self, a: List[int]) -> bool:
        # write your code here
        if a is None or len(a) == 0:
            return False
        current: int = 0
        max_jump_energy: int = 0
        while current < len(a) -1:
            max_jump_energy = max(a[current], max_jump_energy - 1)
            if max_jump_energy < 1:
                return False
            current += 1
        return True


# solution 1-b
# T = O(n), algo: energy-driven move, for in
class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    # T = O(n)
    def can_jump(self, a: List[int]) -> bool:
        # write your code here
        if a is None or len(a) == 0:
            return False
        max_jump_energy: int = 0
        for current in range(len(a) -1):
            max_jump_energy = max(a[current], max_jump_energy - 1)
            if max_jump_energy < 1:
                return False
        return True


# solution 1-c
# T = O(n), algo: energy-driven move + greedy
class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    # T = O(n)
    def can_jump(self, a: List[int]) -> bool:
        # write your code here
        if a is None or len(a) == 0:
            return False
        max_jump_energy: int = 0
        for current in range(len(a) -1):
            max_jump_energy = max(a[current], max_jump_energy - 1)
            if max_jump_energy < 1:
                return False
            if a[current] + max_jump_energy >= len(a) - 1:
                return True
        return True


# solution 2
# T = O(n), algo: energy reachable edge
class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    def can_jump(self, a: List[int]) -> bool:
        # write your code here
        if a is None or len(a) == 0:
            return False
        current: int = 0
        energy_reachable_edge: int = 0
        while True:
            if current <= energy_reachable_edge:
                energy_reachable_edge = max(current + a[current], energy_reachable_edge)
                if energy_reachable_edge >= len(a) -1:
                    return True
                current += 1
            else:
                return False


# solution 3
# T = O(n), algo: range greedy
class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    def can_jump(self, a: List[int]) -> bool:
        # write your code here
        if a is None or len(a) == 0:
            return False
        current: int = 0
        greedy_edge: int = 0
        dyn_edge: int = 0
        greedy_edge = current + a[current]
        while greedy_edge < len(a) -1:
            while current < greedy_edge:
                current += 1
                dyn_edge = max(dyn_edge, current + a[current])
                if dyn_edge >= len(a) - 1:
                    return True
            dyn_edge = max(dyn_edge, current + a[current])
            if dyn_edge == greedy_edge:
                return False
            greedy_edge = dyn_edge
        return True


# solution 4
# T = O(n^2), algo: dp-pre
class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    def can_jump(self, a: List[int]) -> bool:
        # write your code here
        if not a:
            return False
        n: int = len(a)
        res: List[bool] = [False] * n
        res[0] = True
        for current in range(1, n):
            for j in range(current):
                if res[j] == True and j + a[j] >= current:
                    res[current] = True
                    break
        return res[n - 1]

