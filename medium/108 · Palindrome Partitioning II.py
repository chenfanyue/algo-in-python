class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def min_cut(self, s: str) -> int:
        # write your code here
        if not s:
            return 0
        
        cut_records = dict()
        palindromes = self.get_palindromes(s)

        return self.dfs(s, 0, cut_records, palindromes)
    
    def dfs(self, s, start, cut_records, palindromes):
        if start + 1 ==len(s):
            return 0
        if start in cut_records:
            return cut_records[start]
        if (start, len(s) - 1) in palindromes:
            return 0
        
        least_cut = float('inf')
        for end in range(start, len(s)):
            if (start, end) not in palindromes:
                continue
            need_to_cut = 1 + self.dfs(s, end + 1, cut_records, palindromes)
            if need_to_cut < least_cut:
                least_cut = need_to_cut
        
        cut_records[start] = least_cut

        return least_cut

    def get_palindromes(self, s):
        res = set()
        if not s:
            return res
        
        n = len(s)
        for i in range(n):
            left, right = i, i + 1
            self.add_palindromes(s, left, right, res)
            left = right = i
            self.add_palindromes(s, left, right, res)
        
        return res
    
    def add_palindromes(self, s, left, right, res):
        n = len(s)
        while left > -1 and right < n:
            if s[left] == s[right]:
                res.add((left, right))
                left -= 1
                right += 1
            else:
                break

