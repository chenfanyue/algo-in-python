class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def valid_palindrome(self, s: str) -> bool:
        # Write your code here
        if s is None:
            return False
        if len(s) <= 1:
            return True

        left, right = self.stopped_position(s, 0, len(s) - 1)

        if left >= right:
            return True
        return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1)

    def stopped_position(self, s, left, right):
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1

        return left, right

    def is_palindrome(self, s, left, right):
        left, right = self.stopped_position(s, left, right)
        return left >= right
