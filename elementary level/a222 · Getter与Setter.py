class School:
    '''
     * Declare a setter method `setName` which expect a parameter *name*.
    '''
    # write your code here
    def __init__(self):
        self.__name = ''

    def setName(self, name: str):
        self.__name = name

    '''
     * Declare a getter method `getName` which expect no parameter and return
     * the name of this school
    '''
    # write your code here
    def getName(self) -> str:
        return self.__name
