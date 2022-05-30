class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        if target is None or not reader:
            return -1
        
        left, right = self.find_range(reader, target)
        if left == -1:
            return -1
        
        while left < right:
            mid = left + (right - left) // 2
            if reader.get(mid) >= target:
                right = mid
            else:
                left = mid + 1
        if reader.get(left) == target:
            return left
        return -1

    def find_range(self, reader, target):
        if reader.get(0) == target:
            return 0, 0
        
        OVER = 2 ** 31 - 1
        left, offset = 0, 1
        while True:
            while (val := reader.get(left + offset)) != OVER and val < target:
                left += offset
                offset *= 2

            if val == OVER:
                if offset == 1:
                    return -1, -1
                offset //= 2
            else:
                return left, left + offset


class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        if target is None or not reader:
            return -1
        
        left, right = self.find_range(reader, target)
        if left == -1:
            return -1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if reader.get(mid) >= target:
                right = mid
            else:
                left = mid
        if reader.get(left) == target:
            return left
        if reader.get(right) == target:
            return right
        return -1

    def find_range(self, reader, target):
        if reader.get(0) == target:
            return 0, 0

        OVER = 2 ** 31 - 1
        left, offset = 0, 1
        while True:
            while (val := reader.get(left + offset)) != OVER and val < target:
                offset *= 2

            if val == OVER:
                if offset == 1:
                    return -1, -1
                left = left + offset // 2
                offset = 1
            else:
                return left, left + offset


# binary search
class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        if target is None or not reader:
            return -1
        
        left, right = 0, 1
        while reader.get(right) < target:
            right <<= 1
        
        while left < right:
            mid = left + (right - left) // 2
            if reader.get(mid) >= target:
                right = mid
            else:
                left = mid + 1
        if reader.get(left) == target:
            return left
        return -1
