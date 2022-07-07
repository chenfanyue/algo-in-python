stack = []
while root or stack:
    while root:
        stack.append(root)
        root = root.left
    
    root = stack.pop()
    print(root.val, end=' ')
    
    if root.right:
        root = root.right
        continue
    
    root = None
