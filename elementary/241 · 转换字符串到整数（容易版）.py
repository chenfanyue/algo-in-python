class Solution:
    """
    @param target: A string
    @return: An integer
    """
    def string_to_integer(self, target: str) -> int:
        # write your code here
        return int(target)


class Solution:
    """
    @param target: A string
    @return: An integer
    """
    def string_to_integer(self, target: str) -> int:
        # write your code here
        sum = 0
        if target[0] == '-':
            for i in range(1, len(target)):
                sum = sum * 10 - (ord(target[i]) - ord('0'))
            return sum
        for c in target:
            sum = sum * 10 + (ord(c) - ord('0'))
        return sum


class Solution:
    """
    @param target: A string
    @return: An integer
    """
    def string_to_integer(self, target: str) -> int:
        # write your code here
        sum = 0
        if target[0] == '-':
            for i in range(1, len(target)):
                sum = sum * 10 - int(target[i])
            return sum
        for c in target:
            sum = sum * 10 + int(c)
        return sum


class Solution:
    """
    @param target: A string
    @return: An integer
    """
    def string_to_integer(self, target: str) -> int:
        # write your code here
        res = 0
        positive = 1
        if target[0] == '-':
            positive = -1
            target = target[1:] # 时间复杂度
        for c in target:
            res = res * 10 + (ord(c) - ord('0'))
        return res * positive
