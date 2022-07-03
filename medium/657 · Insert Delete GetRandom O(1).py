class RandomizedSet:
    
    def __init__(self):
        self.arr, self.mapping = [], {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        if val in self.mapping:
            return False
        
        self.arr.append(val)
        self.mapping[val] = len(self.arr) - 1

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        if val not in self.mapping:
            return False
        
        idx = self.mapping[val]
        last = self.arr[-1]
        self.arr[idx] = last
        self.arr.pop()

        self.mapping.pop(val)
        self.mapping[last] = idx

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        import random
        idx = random.randrange(len(self.arr))
        # idx = random.randint(0, len(self.arr) - 1)
        return self.arr[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
