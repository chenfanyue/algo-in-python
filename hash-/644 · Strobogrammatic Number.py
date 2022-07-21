class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def is_strobogrammatic(self, num: str) -> bool:
        if not num:
            return True

        s = set([('6', '9'), ('9', '6'), ('8', '8'), ('1', '1'), ('0', '0')])
        end = len(num) - 1
        mid = end >> 1
        for i in range(mid + 1):
            if (num[i], num[end - i]) not in s:
                return False
        
        return True
