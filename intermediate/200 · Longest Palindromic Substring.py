class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longest_palindrome(self, s: str) -> str:
        # write your code here
        if not s:
            return s

        n = len(s)
        left = right = -1
        length = 0
        for start in range(n):
            if n - start <= length:
                break
            for end in range(n - 1, start - 1, -1):
                if self.is_palindrome(s, start, end):
                    length_here = end - start + 1
                    if length_here > length:
                        length = length_here
                        left, right = start, end
                    break

        return s[left : right + 1]

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

