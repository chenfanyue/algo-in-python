"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
# 对象按属性映射成元组，元组按成员重组成对象
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        res = []
        heap = []

        for i, arr in enumerate(intervals):
            if not arr:
                continue
            heapq.heappush(heap, (arr[0].start, arr[0].end, i, 1))

        while heap:
            start, end, i, j = heapq.heappop(heap)
            self.push_back(res, Interval(start, end))
            if j < len(intervals[i]):
                heapq.heappush(heap, (intervals[i][j].start, intervals[i][j].end, i, j + 1))
        
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


class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        res = []
        heap = []

        for i, arr in enumerate(intervals):
            if not arr:
                continue
            heapq.heappush(heap, (arr[0].start, arr[0].end, i, 1, arr[0]))

        while heap:
            _, _, i, j, v = heapq.heappop(heap)
            self.push_back(res, v)
            if j < len(intervals[i]):
                heapq.heappush(heap, (intervals[i][j].start, intervals[i][j].end, i, j + 1, intervals[i][j]))
        
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
