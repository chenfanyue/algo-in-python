class DLinkedNode:
    def __init__(self, key=None, val=None, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.key_node = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.key_node:
            return -1
        
        node = self.key_node.get(key)
        self.move_to_head(node)

        return node.val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key in self.key_node:
            node = self.key_node.get(key)
            node.val = value
            self.move_to_head(node)
            return
        
        node = DLinkedNode(key, value)
        self.key_node[key] = node
        self.insert_at_head(node)
        self.size += 1

        if self.size > self.capacity:
            node_to_remove = self.tail.prev
            self.remove_node(node_to_remove)
            self.key_node.pop(node_to_remove.key)
    
    def remove_node(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
    
    def insert_at_head(self, node):
        node.prev = self.head
        node.nxt = self.head.nxt
        self.head.nxt = node
        node.nxt.prev = node
    
    def move_to_head(self, node):
        self.remove_node(node)
        self.insert_at_head(node)


from collections import OrderedDict

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.cache:
            return -1
        
        val = self.cache.pop(key)
        self.cache[key] = val
        
        return val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            return
        
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
