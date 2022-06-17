class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def is_valid_parentheses(self, s: str) -> bool:
        # write your code here
        if not s:
            return False
        
        stack = []
        for ch in s:
            if self.is_left_side(ch):
                stack.append(ch)
                continue
            if not stack or not self.paired(stack[-1], ch):
                return False
            stack.pop()
        
        if stack:
            return False
        return True

    def is_left_side(self, ch: str) -> bool:
        return ch == '(' or ch == '[' or ch == '{'
    
    def paired(self, a, b):
        if a == '(' and b == ')':
            return True
        if a == '[' and b == ']':
            return True
        if a == '{' and b == '}':
            return True
        return False
