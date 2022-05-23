# 描述
# 和题目 左旋右旋迭代器 类似，在本题中，你将得到一个列表vecs，其中包括 k 个一维向量。
# 你的任务是通过 next 函数一个个地返回向量中的元素，按照 vecs[0][0], vecs[1][0]... vecs[k - 1][0], vecs[0][1], vecs[1][1]... vecs[k - 1][1], vecs[0][2], vecs[1][2]... vecs[k - 1][2]... 的顺序进行迭代。
# 样例1
# 输入: k = 3
# vecs = [
#     [1,2,3],
#     [4,5,6,7],
#     [8,9],
# ]
# 输出: [1,4,8,2,5,9,3,6,7]
# Follow up Zigzag Iterator: What if you are given k 1d vectors? How well can your code be extended to such cases? The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".


class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        # do intialization if necessary
        self.que = collections.deque()
        for vec in vecs:
            if vec:
                reversed_vec = vec[::-1]
                self.que.appendleft(reversed_vec)

    """
    @return: An integer
    """
    def _next(self):
        # write your code here
        vec = self.que.pop()
        val = vec.pop()
        if vec:
            self.que.appendleft(vec)
        return val

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return len(self.que) > 0

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result

