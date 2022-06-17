class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        # Write your code here
        return source.find(target)


class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        # Write your code here
        if len(target) == 0:
            return 0
        n, m = len(source), len(target)
        if m > n:
            return -1
        if m == n:
            if source == target:
                return 0
            return -1
        
        i = 0
        end = n - m + 1
        while i < end:
            if source[i : i + m] == target:
                return i
            i += 1
        return -1


class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        # Write your code here
        n, m = len(source), len(target)
        if len(target) == 0:
            return 0

        if m > n:
            return -1

        if m == n:
            if source == target:
                return 0
            return -1
        
        i = 0
        while i < n - m + 1:
            j = 0
            while j < m:
                if source[i + j] != target[j]:
                    break
                j += 1
            if j == m:
                return i
            i += 1
        return -1


class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        # Write your code here
        n, m = len(source), len(target)
        if len(target) == 0:
            return 0

        if m > n:
            return -1

        if m == n:
            if source == target:
                return 0
            return -1
        
        for i in range(n - m + 1):
            j = 0
            while j < m:
                if source[i + j] != target[j]:
                    break
                j += 1
            if j == m:
                return i
        return -1


class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        # Write your code here
        if source == None or target == None:
            return -1
            
        m = len(target)
        if m == 0:
            return 0
            
        BASE = 1000000
        # power = (31 ** m) % BASE
        # 不建议上面的写法, 先算完31 ** m再取模效率太低, 建议在乘的过程中进行取模
        power = 1
        for i in range(m):
            power = (power * 31) % BASE
        
        targetCode = 0
        for char in target:
            targetCode = (targetCode * 31 + ord(char)) % BASE
            
        hashCode = 0
        for i in range(len(source)):
            hashCode = (hashCode * 31 + ord(source[i])) % BASE
            if i < m - 1:
                continue
            
            if i >= m:
                hashCode = hashCode - (power * ord(source[i - m]) % BASE)
                if hashCode < 0:
                    hashCode += BASE
                    
            if hashCode == targetCode:
                if source[i - m + 1: i + 1] == target:
                    return i - m + 1
            
        return -1
