class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_palindrome(self, s: str) -> bool:
        # write your code here
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1

        return True


class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_palindrome(self, s: str) -> bool:
        # write your code here
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left >= right:
                return True
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1

        return True


class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_palindrome(self, s: str) -> bool:
        # write your code here
        l, r = 0, len(s) - 1
        while True:
            while l < r and self.not_alnum(s[l]):
                l += 1
            if l >= r:
                return True
            while l < r and self.not_alnum(s[r]):
                r -= 1
            if l >= r:
                return True
            if self.not_equal(s[l], s[r]):
                return False
            l += 1
            r -= 1
        
    def not_alnum(self, char):
        return not ('A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9')
    
    def not_equal(self, cha, chb):
        return not (cha == chb or (self.is_alpha(cha) and self.is_alpha(chb) and abs(ord(cha) - ord(chb)) == 32))

    def is_alpha(self, char):
        return 'A' <= char <= 'Z' or 'a' <= char <= 'z'


class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_palindrome(self, s: str) -> bool:
        # write your code here
        arr = []
        for i in range(len(s)):
            char = s[i]
            if ('A' <= char <= 'Z'):
                arr.append(char.lower())
            if ('a' <= char <= 'z' or '0' <= char <= '9'):
                arr.append(char)

        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True


