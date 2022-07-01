from typing import (
    List,
)

# real time algo, light-weight
class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def first_unique_number(self, nums: List[int], number: int) -> int:
        # Write your code here
        tail = dummy = ListNode(0)
        num_to_prev = {}
        duplicates = set()

        for num in nums:
            self.deal_num(num, duplicates, num_to_prev, tail)
            if num == number:
                break
        else:
            return -1
        
        return self.get_first_unique(dummy)
    
    def deal_num(self, num, duplicates, num_to_prev, tail):
        if num in duplicates:
            return
        
        if num in num_to_prev:
            self.deduplicate(num, duplicates, num_to_prev, tail)
            return
        
        self.add_num(num, num_to_prev, tail)

    def deduplicate(self, num, duplicates, num_to_prev, tail):
        prev = num_to_prev[num]

        prev.nxt = prev.nxt.nxt

        num_to_prev.pop(num)
        if prev.nxt:
            num_to_prev[prev.nxt.val] = prev
        else:
            tail = prev
        
        duplicates.add(num)
    
    def add_num(self, num, num_to_prev, tail):
        num_to_prev[num] = tail
        tail.nxt = ListNode(num)
        tail = tail.nxt
    
    def get_first_unique(self, dummy):
        if dummy.nxt:
            return dummy.nxt.val
        
        return -1


# real time algo, heavy
class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class UniqueList:
    def __init__(self):
        self.tail = self.dummy = ListNode(0)

class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def first_unique_number(self, nums: List[int], number: int) -> int:
        # Write your code here
        unique_list = UniqueList()
        num_to_prev = {}
        duplicates = set()

        for num in nums:
            self.deal_num(num, duplicates, num_to_prev, unique_list)
            if num == number:
                break
        else:
            return -1
        
        return self.get_first_unique(unique_list)
    
    def deal_num(self, num, duplicates, num_to_prev, unique_list):
        if num in duplicates:
            return
        
        if num in num_to_prev:
            self.deduplicate(num, duplicates, num_to_prev, unique_list)
            return
        
        self.add_num(num, num_to_prev, unique_list)

    def deduplicate(self, num, duplicates, num_to_prev, unique_list):
        prev = num_to_prev[num]

        prev.nxt = prev.nxt.nxt

        num_to_prev.pop(num)
        if prev.nxt:
            num_to_prev[prev.nxt.val] = prev
        else:
            unique_list.tail = prev
        
        duplicates.add(num)
    
    def add_num(self, num, num_to_prev, unique_list):
        num_to_prev[num] = unique_list.tail
        unique_list.tail.nxt = ListNode(num)
        unique_list.tail = unique_list.tail.nxt
    
    def get_first_unique(self, unique_list):
        if unique_list.dummy.nxt:
            return unique_list.dummy.nxt.val
        
        return -1
    



# 归零法, non real time
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def first_unique_number(self, nums: List[int], number: int) -> int:
        # Write your code here
        record = {}
        arr, i = [], 0
        for num in nums:
            if num in record:
                arr[record[num]] = None
                arr.append(None)
            else:
                record[num] = i
                arr.append(num)
            if num == number:
                break
            i += 1
        else:
            return -1
        
        for val in arr:
            if val is not None:
                return val


# 变量值赋双重含义, non real time
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def first_unique_number(self, nums: List[int], number: int) -> int:
        # Write your code here
        record = {}
        i = 0
        for num in nums:
            if num in record:
                record[num] = sys.maxsize
            else:
                record[num] = i
            if num == number:
                break
            i += 1
        else:
            return -1
        
        first_unique_index = sys.maxsize
        first_unique = None
        for num, i in record.items():
            if i < first_unique_index:
                first_unique_index = i
                first_unique = num
        
        return first_unique
                

# counting times, non real time
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def first_unique_number(self, nums: List[int], number: int) -> int:
        # Write your code here
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if num == number:
                break
        else:
            return -1
            
        for num in counter:
            if counter[num] == 1:
                return num
