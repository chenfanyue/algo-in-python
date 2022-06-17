class Solution:
    """
    @param s: a string
    @return: a string after capitalizes the first letter
    """
    def capitalizes_first(self, s: str) -> str:
        # Write your code here
        if s == '':
            return s
        # if len(s) == 1:
        #     return s.upper()
        
        arr = list(s)
        arr[0] = arr[0].upper()
        for i in range(1, len(arr)):
            if arr[i-1] == ' ' and arr[i] != ' ':
                arr[i] = arr[i].upper()
        return ''.join(arr)


class Solution:
    """
    @param s: a string
    @return: a string after capitalizes the first letter
    """
    def capitalizes_first(self, s: str) -> str:
        # Write your code here
        arr = s.split(' ')
        for i in range(len(arr)):
            arr[i] = arr[i].capitalize()
        return ' '.join(arr)
