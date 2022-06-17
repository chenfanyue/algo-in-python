from typing import (
    List,
)

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        hashdict = dict()
        for i in range(len(numbers)):
            if (val := target - numbers[i]) in hashdict:
                return [hashdict[val], i]
            hashdict[numbers[i]] = i
        
        return [-1, -1]


class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        if not numbers:
            return [-1, -1]
        
        numbers = [(num, i) for (i, num) in enumerate(numbers)]
        numbers.sort()

        left, right = 0, len(numbers) - 1
        while left < right:
            val = numbers[left][0] + numbers[right][0]
            if val > target:
                right -= 1
            elif val < target:
                left += 1
            else:
                return sorted([numbers[left][1], numbers[right][1]])

        return [-1, -1]
