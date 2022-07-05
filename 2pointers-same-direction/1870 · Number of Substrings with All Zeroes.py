# the best solution, not 2pointers
class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def string_count(self, string: str) -> int:
        if not string:
            return 0
        
        last = -1
        arr = list(string) + ['1'] # dummy '1'
        n = len(arr)
        res = 0
        
        for i in range(n):
            if arr[i] != '1':
                continue
            number = i - last - 1
            res += (number + 1) * number // 2
            last = i
        
        return res


class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def string_count(self, string: str) -> int:
        if not string:
            return 0
        
        i, j = 0, 1
        n = len(string)
        res = 0
        
        while i < n:
            if string[i] != '0':
                i += 1
                continue
            j = max(j, i + 1)
            while j < n and string[j] == '0':
                j += 1
            res += (j - i + 1) * (j - i) // 2
            i = j + 1
        
        return res


class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def string_count(self, string: str) -> int:
        if not string:
            return 0
        
        last = -1
        n = len(string)
        res = 0
        
        for i in range(n):
            if string[i] != '1':
                continue
            number = i - last - 1
            res += (number + 1) * number // 2
            last = i
        
        if string[n - 1] == '0':
            number = n - last - 1
            res += (number + 1) * number // 2
        
        return res


class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def string_count(self, string: str) -> int:
        if not string:
            return 0
        
        j, n = 1, len(string)
        res = 0
        for i in range(n):
            if string[i] != '0':
                continue
            j = max(j, i + 1)
            while j < n and string[j] == '0':
                j += 1
            res += j - i
        
        return res


