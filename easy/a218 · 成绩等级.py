class Student:
    name: str = ''
    score: int = 0

    
    '''
     * Declare a constructor expect a name as a parameter.
    '''
    def __init__(self, name: str):
        self.name = name
    
    '''
     * Declare a public method `getLevel` to get the level(char) of this student.
    '''
    def getLevel(self) -> str:
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 60:
            return 'C'
        else:
            return 'D'


class Student:
    name: str = ''
    score: int = 0

    
    '''
     * Declare a constructor expect a name as a parameter.
    '''
    def __init__(self, name: str):
        self.name = name
    
    '''
     * Declare a public method `getLevel` to get the level(char) of this student.
    '''
    def getLevel(self) -> str:
        if self.score >= 90:
            return 'A'
        elif 80 <= self.score < 90:
            return 'B'
        elif 60 <= self.score < 80:
            return 'C'
        else:
            return 'D'
