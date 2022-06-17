class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longest_palindrome(self, s: str) -> int:
        # write your code here
        char_set = set()
        pairs = 0
        for i in range(len(s)):
            ch = s[i]
            if ch not in char_set:
                char_set.add(ch)
            else:
                char_set.remove(ch)
                pairs += 1
        
        if char_set:
            return pairs * 2 + 1
        else:
            return pairs * 2


# recommended
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longest_palindrome(self, s: str) -> int:
        # write your code here
        char_set = set()
        for ch in s:
            if ch not in char_set:
                char_set.add(ch)
            else:
                char_set.remove(ch)
        
        n = len(char_set)
        if n == 0:
            return len(s)
        else:
            return len(s) - n + 1


# recommended
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longest_palindrome(self, s: str) -> int:
        # write your code here
        char_dict = dict()
        for ch in s:
            if ch not in char_dict:
                char_dict[ch] = True
            else:
                del char_dict[ch]
        
        n = len(char_dict)
        if n == 0:
            return len(s)
        else:
            return len(s) - n + 1


class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longest_palindrome(self, s: str) -> int:
        # write your code here
        char_set = set()
        for i in range(len(s)):
            ch = s[i]
            if ch not in char_set:
                char_set.add(ch)
            else:
                char_set.remove(ch)
        
        n = len(char_set)
        if n == 0:
            return len(s)
        else:
            return len(s) - n + 1


class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longest_palindrome(self, s: str) -> int:
        # write your code here
        char_set = set()
        pairs = 0
        for ch in s:
            if ch in char_set:
                char_set.remove(ch)
                pairs += 1
            else:
                char_set.add(ch)
        
        if char_set:
            return pairs * 2 + 1
        else:
            return pairs * 2


# greedy
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longest_palindrome(self, s: str) -> int:
        # write your code here
        res = 0
        cnt = collections.Counter(s)

        for val in cnt.values():
            res += val // 2 * 2
        
        if len(s) > res:
            res += 1
        
        return res


