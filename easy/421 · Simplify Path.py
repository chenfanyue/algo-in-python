class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """
    def simplify_path(self, path: str) -> str:
        # write your code here
        arr = path.split('/')
        stack = []

        for sub in arr:
            if sub == '.' or sub == '':
                continue
            elif sub == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(sub)
        
        if not stack:
            return '/'
        return '/' + '/'.join(stack)


