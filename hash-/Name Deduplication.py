from typing import (
    List,
)

class Solution:
    """
    @param names: a string array
    @return: a string array
             we will sort your return value in output
    """
    def name_deduplication(self, names: List[str]) -> List[str]:
        s = {v.lower() for v in names}

        return list(s)
