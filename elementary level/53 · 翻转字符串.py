class Solution:
    """
    @param s: A string
    @return: A string
    """
    def reverse_words(self, s: str) -> str:
        # write your code here
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1
        
        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1
            
        deq, cnt = collections.deque(), 0
        # 将单词 push 到队列的头部
        while left <= right:
            if s[left] != ' ':
                cnt += 1
            else:
                if cnt:
                    deq.appendleft(s[left - cnt : left])
                    cnt = 0
            left += 1
        deq.appendleft(s[left - cnt : left])
        
        return ' '.join(deq)


class Solution:
    """
    @param s: A string
    @return: A string
    """
    def reverse_words(self, s: str) -> str:
        # write your code here
        if len(s) == 0:
            return s
        
        arr = s.split()
        arr2 = [item for item in arr if arr != '']
        return ' '.join(arr2[::-1])


class Solution:
    """
    @param s: A string
    @return: A string
    """
    def reverse_words(self, s: str) -> str:
        # write your code here
        if len(s) == 0:
            return s
        
        cnt = 0 # cnt represents word length
        arr  = []
        n = len(s)
        for i in range(n):
            if s[i] != ' ':
                cnt += 1
            else:
                if cnt != 0:
                    arr.append(s[i - cnt : i])
                    cnt = 0
        if cnt != 0:
            arr.append(s[n - cnt : n])

        return ' '.join(arr[::-1])


class Solution:
    """
    @param s: A string
    @return: A string
    """
    def reverse_words(self, s: str) -> str:
        # write your code here
        if len(s) == 0:
            return s
        
        word = []
        arr  = []
        for i in range(len(s)):
            if s[i] != ' ':
                word.append(s[i])
            else:
                if len(word) > 0:
                    arr.append(''.join(word))
                    word = []
        if len(word) > 0:
            arr.append(''.join(word))

        return ' '.join(arr[::-1])


# opposed to expected, runs slower
class Solution:
    """
    @param s: A string
    @return: A string
    """
    def reverse_words(self, s: str) -> str:
        # write your code here
        if len(s) == 0:
            return s
        
        cnt = 0 # cnt represents word length
        arr  = []
        for i in range(len(s) -1, -1, -1):
            if s[i] != ' ':
                cnt += 1
            else:
                if cnt != 0:
                    arr.append(s[i + 1 : i + cnt + 1])
                    cnt = 0
        if cnt != 0:
            arr.append(s[0 : cnt])

        return ' '.join(arr)


class Solution:
    """
    @param s: A string
    @return: A string
    """
    def reverse_words(self, s: str) -> str:
        # write your code here
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1
        
        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1
            
        deq, word = collections.deque(), []
        # 将单词 push 到队列的头部
        while left <= right:
            if s[left] != ' ':
                word.append(s[left])
            else:
                if word:
                    deq.appendleft(''.join(word))
                    word = []
            left += 1
        deq.appendleft(''.join(word))
        
        return ' '.join(deq)


class Solution:
    """
    @param s: A string
    @return: A string
    """
    def reverse_words(self, s: str) -> str:
        # write your code here
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1

        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1

        if left > right:
            return ''
        
        deq, first = collections.deque(), -1
        # 将单词 push 到队列的头部
        # first同时充当周期状态量和单词第一个字的下标
        while left <= right:
            if s[left] != ' ':
                if first == -1:
                    first = left
            else:
                if first != -1:
                    deq.appendleft(s[first : left])
                    first = -1
            left += 1
        deq.appendleft(s[first : left])
        
        return ' '.join(deq)
