# 归并排序一趟清完
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, a, m, b, n):
        p1, p2 = m - 1, n - 1
        tail = m + n - 1

        while p1 > -1 or p2 > -1:
            if p1 == -1:
                val = b[p2]
                p2 -= 1
            elif p2 == -1:
                val = a[p1]
                p1 -= 1
            elif a[p1] > b[p2]:
                val = a[p1]
                p1 -= 1
            else:
                val = b[p2]
                p2 -= 1
            a[tail] = val
            tail -= 1


# 归并排序分两个阶段完成
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, a, m, b, n):
        p1, p2 = m - 1, n - 1
        tail = m + n - 1

        while p1 > -1 and p2 > -1:
            if a[p1] > b[p2]:
                val = a[p1]
                p1 -= 1
            else:
                val = b[p2]
                p2 -= 1
            a[tail] = val
            tail -= 1
        
        if p1 == -1:
            while p2 > -1:
                a[tail] = b[p2]
                p2 -= 1
                tail -= 1
        if p2 == -1:
            while p1 > -1:
                a[tail] = a[p1]
                p1 -= 1
                tail -= 1





