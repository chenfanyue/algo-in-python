# list and set
class TwoSum:
    def __init__(self):
        self.data = list()
    
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        self.data.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        helper = set()
        for v in self.data:
            if (value - v) in helper:
                return True
            helper.add(v)
        
        return False


# dict
# class TwoSum(object):
class TwoSum:
    def __init__(self):
        self.count = {}
    
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        self.count[number] = self.count.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for number in self.count:
            if value - number in self.count and \
                (value - number != number or self.count[number] > 1):
                return True
        
        return False
    # def find(self, value):
    #     # write your code here
    #     for num1 in self.count:
    #         num2 = value - num1
    #         desired_cnt = 2 if num2 == num1 else 1
    #         if self.count.get(num2, 0) >= desired_cnt:
    #             return True
        
    #     return False


# sorted array and left/right pointers
class TwoSum:
    
    def __init__(self):
        self.nums = []
        
    def add(self, number):
        self.nums.append(number)
        index = len(self.nums) - 1
        while index > 0 and self.nums[index - 1] > self.nums[index]:
            temp = self.nums[index - 1]
            self.nums[index - 1] = self.nums[index]
            self.nums[index] = temp
            index -= 1

    def find(self, value):
        left, right = 0, len(self.nums) - 1
        while left < right:
            two_sum = self.nums[left] + self.nums[right]
            if two_sum < value:
                left += 1
            elif two_sum > value:
                right -= 1
            else:
                return True
        return False
