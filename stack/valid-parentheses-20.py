class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for i in range(len(s)):
            match s[i]:
                case '(' | '[' | '{':
                    stack.append(pairs[s[i]])
                case _:
                    if not stack or stack[-1] != s[i]:
                        return False
                    stack.pop()
        
        return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for i in range(n):
            if s[i] in pairs:
                if not stack or stack[-1] != pairs[s[i]]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])

        return not stack
