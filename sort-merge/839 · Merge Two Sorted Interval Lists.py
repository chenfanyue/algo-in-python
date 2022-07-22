from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def merge_two_interval(self, list1: List[Interval], list2: List[Interval]) -> List[Interval]:
        if not list1 and not list2:
            return []
        if not list2:
            return list1
        if not list1:
            return list2

        res = []
        i = j = 0

        while i < len(list1) and j < len(list2):
            if list1[i].start < list2[j].start:
                self.push_back(res, list1[i])
                i += 1
            else:
                self.push_back(res, list2[j])
                j += 1
        while i < len(list1):
            self.push_back(res, list1[i])
            i += 1
        while j < len(list2):
            self.push_back(res, list2[j])
            j += 1

        return res

    def push_back(self, res, interval):
        if not res:
            res.append(interval)
            return

        last = res[-1]
        if interval.start > last.end:
            res.append(interval)
            return

        last.end = max(last.end, interval.end)

