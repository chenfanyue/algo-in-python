class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, r = 0, -1
        j = i = 0
        while i < len(s):
            while j+1 < len(s) and s[j+1] == s[i]:
                j += 1
            iNext = j + 1
            while i-1 >= 0 and j+1 < len(s) and s[i-1] == s[j+1]:
                i -= 1
                j += 1
            if j-i > r-l:
                l, r = i, j
            j = i = iNext
        return s[l : r+1]


class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longest_palindrome(self, s: str) -> str:
        # write your code here
        if not s:
            return s

        longest = ''
        length = 0
        for i in range(len(s)):
            sub = self.find_palindrome(s, i, i)
            if len(sub) > length:
                longest = sub
                length = len(sub)
            sub = self.find_palindrome(s, i, i + 1)
            if len(sub) > length:
                longest = sub
                length = len(sub)
        
        return longest

    def find_palindrome(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        
        return s[left + 1 : right]


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


# runs fast but not recommended because of poor readability
class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longest_palindrome(self, s: str) -> str:
        # write your code here
        if not s:
            return s

        left, right = -1, -1
        length = 0
        for i in range(len(s)):
            sub_left, sub_right = self.find_palindrome(s, i, i)
            if (length_here := sub_right - sub_left + 1) > length:
                left, right = sub_left, sub_right
                length = length_here
            sub_left, sub_right = self.find_palindrome(s, i, i + 1)
            if (length_here := sub_right - sub_left + 1) > length:
                left, right = sub_left, sub_right
                length = length_here
        
        return s[left : right + 1]

    def find_palindrome(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        
        return left + 1, right - 1


