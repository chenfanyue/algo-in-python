class Solution:
    """
    @param a: a string
    @param b: a string
    @return: return the sum of two strings
    """
    def sumof_two_strings(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a
        shorter, longer = len(a), len(b)
        gap = longer - shorter

        arr_a = [0] * longer
        arr_b = [0] * longer
        for i in range(longer):
            if i < gap:
                arr_a[i] = 0
            else:
                arr_a[i] = int(a[i - gap])
        for i in range(longer):
            arr_b[i] = int(b[i])

        res = []
        for i in range(longer):
            val = arr_a[i] + arr_b[i]
            res.append(str(val))
        
        return ''.join(res)


class Solution:
    """
    @param a: a string
    @param b: a string
    @return: return the sum of two strings
    """
    def sumof_two_strings(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a
        shorter, longer = len(a), len(b)
        gap = longer - shorter

        arr_a = []
        arr_b = []
        for _ in range(gap):
            arr_a.append(0)
        for ch in a:
            arr_a.append(int(ch))
        for ch in b:
            arr_b.append(int(ch))

        res = []
        for i in range(longer):
            val = arr_a[i] + arr_b[i]
            res.append(str(val))
        
        return ''.join(res)



