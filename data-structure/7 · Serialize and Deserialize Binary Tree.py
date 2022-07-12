"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        if not root:
            return '{}'
        
        q = [root]
        idx = 0
        while idx < len(q):
            cur = q[idx]
            if cur:
                q.append(cur.left)
                q.append(cur.right)
            idx += 1
        
        while q[-1] is None:
            q.pop()
        
        return '{%s}' % ','.join([
            str(node.val) if node else '#'
            for node in q
        ])

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        if data == '{}':
            return None
        
        data = data[1:-1].split(',')
        root = TreeNode(int(data[0]))
        q = [root]
        idx = 0
        left = True

        for v in data[1:]:
            node = None if v == '#' else TreeNode(int(v))
            if left:
                q[idx].left = node
            else:
                q[idx].right = node
            if node:
                q.append(node)
            
            if not left:
                idx += 1
            left = not left
        
        return root
