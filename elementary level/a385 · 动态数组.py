class ArrayListManager:
    '''
     * @param n: You should generate an array list of n elements.
     * @return: The array list your just created.
    '''
    def create(self, n):
        # Write your code here
        return [i for i in range(n)]
    
    
    '''
     * @param list: The list you need to clone
     * @return: A deep copyed array list from the given list
    '''
    def clone(self, list):
        # Write your code here
        return list[:]
    
    
    '''
     * @param list: The array list to find the kth element
     * @param k: Find the kth element
     * @return: The kth element
    '''
    def get(self, list, k):
        # Write your code here
        return list[k]
    
    
    '''
     * @param list: The array list
     * @param k: Find the kth element, set it to val
     * @param val: Find the kth element, set it to val
    '''
    def set(self, list, k, val):
        # write your code here
        if k >= len(list):
            list.append(val)
        list[k] = val
    
    
    '''
     * @param list: The array list to remove the kth element
     * @param k: Remove the kth element
    '''
    def remove(self, list, k):
        # write tour code here
        return list.pop(k)
        # return list.remove(k)
        # del list[k]
  
    
    '''
     * @param list: The array list.
     * @param val: Get the index of the first element that equals to val
     * @return: Return the index of that element
    '''
    def indexOf(self, list, val):
        # Write your code here
        if val in list:
            return list.index(val)
        return -1
        # for i in range(len(list)):
        #     if list[i] == val:
        #         return i
        # return -1

