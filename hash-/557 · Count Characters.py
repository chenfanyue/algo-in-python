class Solution:
    """
    @param: : a string
    @return: Return a hash map
    """
    def countCharacters(self, a: str):
        res = dict()
        
        for i in range(len(a)):
            res[a[i]] = res.get(a[i], 0) + 1

        return res


from collections import defaultdict

class Solution:
    """
    @param: : a string
    @return: Return a hash map
    """
    def countCharacters(self, a: str):
        res = defaultdict(int)
        
        # for v in list(a):
        #     res[v] += 1
        for i in range(len(a)):
            res[a[i]] += 1

        return res

