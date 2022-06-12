class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expression_expand(self, s: str) -> str:
        # write your code here
        if not s:
            return s
        
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
                continue

            arr = []
            while (top := stack.pop()) != '[':
                arr.append(top)
            arr.reverse()
            
            repeat = 0
            base = 1
            while stack and stack[-1].isdigit():
                repeat += int(stack.pop()) * base
                base *= 10

            # stack.append(''.join(arr) * repeat)
            for _ in range(repeat):
                stack.extend(arr)
        
        return ''.join(stack)


class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expression_expand(self, s: str) -> str:
        # write your code here
        if not s:
            return s
        
        stack = []
        for ch in s:
            if ch.isalnum() or ch == '[':
                stack.append(ch)
            if ch == ']':
                arr = []
                while (top := stack.pop()) != '[':
                    arr.append(top)
                arr.reverse()
                
                digit = []
                while stack and stack[-1].isdigit():
                    digit.append(stack.pop())
                digit.reverse()
                digit = ''.join(digit)
                digit = int(digit)
                
                # stack.append(''.join(arr) * digit)
                for _ in range(digit):
                    stack.extend(arr)
        
        return ''.join(stack)


