from typing import (
    List,
)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        # write your code here
        if not numbers or len(numbers) < 3:
            return [[]]
        
        negative = dict()
        positive = dict()
        complete = dict()
        for num in numbers:
            complete[num] = complete.get(num, 0) + 1
            if num < 0:
                negative[num] = negative.get(num, 0) + 1
            if num > 0:
                positive[num] = positive.get(num, 0) + 1
        
        tmp = set()
        for a in negative:
            for c in positive:
                self.add_triplet(tmp, a, c, complete)
        
        res = [list(e) for e in tmp]
        if complete.get(0, 0) >= 3:
            res.append([0, 0, 0])
        
        return res
    
    def add_triplet(self, tmp, a, c, complete):
        can_add = False
        if (b := -(a + c)) in complete:
            if b == a and complete[a] >= 2:
                can_add = True
            if b == c and complete[c] >= 2:
                can_add = True
            if b != a and b != c:
                can_add = True
        if can_add:
            triplet = [a, b, c]
            triplet.sort()
            tmp.add(tuple(triplet))


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        # write your code here
        if not numbers or len(numbers) < 3:
            return [[]]

        numbers.sort()

        res = set()
        for i in range(len(numbers) - 2):
            if numbers[i] > 0:
                break
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            self.add_triplet(res, numbers, i)

        return [list(e) for e in res]

    def add_triplet(self, res, numbers, i):
        a = numbers[i]
        left, right =  i + 1, len(numbers) - 1
        while left < right:
            if numbers[right] < 0:
                break
            val = numbers[left] + numbers[right]
            if val > -a:
                right -= 1
            elif val < -a:
                left += 1
            else:
                res.add((a, numbers[left], numbers[right]))
                left += 1
                right -= 1


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        # write your code here
        if not numbers or len(numbers) < 3:
            return [[]]

        numbers.sort()

        res = []
        for i in range(len(numbers) - 2):
            if numbers[i] > 0:
                break
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            self.add_triplet(res, numbers, i)

        return res

    def add_triplet(self, res, numbers, i):
        a = numbers[i]
        last_triplet = [None, None, None]
        left, right =  i + 1, len(numbers) - 1
        while left < right:
            if numbers[right] < 0:
                break
            val = numbers[left] + numbers[right]
            if val > -a:
                right -= 1
            elif val < -a:
                left += 1
            else:
                triplet = [a, numbers[left], numbers[right]]
                if triplet != last_triplet:
                    res.append(triplet)
                    last_triplet = triplet
                left += 1
                right -= 1
