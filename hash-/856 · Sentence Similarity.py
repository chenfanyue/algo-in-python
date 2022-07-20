from typing import (
    List,
)

class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    def is_sentence_similarity(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if not words1 and not words2:
            return True
        if not words1 or not words2:
            return False
        if len(words1) != len(words2):
            return False

        s = set()
        for pair in pairs:
            s.add((pair[0], pair[1]))

        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            if (words1[i], words2[i]) not in s and (words2[i], words1[i]) not in s:
                return False
        
        return True
