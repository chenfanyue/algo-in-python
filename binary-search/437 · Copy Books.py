from typing import (
    List,
)

# 二分答案，用第三方条件验证反馈
class Solution:
    """
    @param books: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copy_books(self, books: List[int], k: int) -> int:
        if not books:
            return 0
        if k >= len(books):
            return max(books)
        
        left, right = max(books), sum(books)
        while left + 1 < right:
            mid = (left + right) >> 1
            if self.need_workers(books, mid) <= k:
                right = mid
            else:
                left = mid
        if self.need_workers(books, left) <= k:
            return left
        return right

    def need_workers(self, books, max_work):
        work = 0
        cnt = 0
        for book in books:
            if book == max_work:
                if work == 0:
                    cnt += 1
                    continue
                else:
                    cnt += 2
                    work = 0
                    continue
            if work + book == max_work:
                cnt += 1
                work = 0
                continue
            if work + book < max_work:
                work += book
                continue
            if work + book > max_work:
                cnt += 1
                work = book
        
        if work:
            cnt += 1
        
        return cnt


# time limit exceeded
class Solution:
    """
    @param books: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copy_books(self, books: List[int], k: int) -> int:
        if not books:
            return 0
        if k >= len(books):
            return max(books)
        
        longest = len(books) - k + 1
        local_max = 0
        record = {'min_global_max': 0}
        cut = 0
        self.dfs(books, longest, 0, cut, k, local_max, record)

        return record['min_global_max']
    
    def dfs(self, books, longest, start, cut, k, local_max, record):
        if cut == k:
            if start == len(books):
                record['min_global_max'] = local_max
                return
            else:
                return
        if cut < k and start >= len(books):
            return
        if cut > k:
            return
        
        job = 0
        for i in range(start, start + longest):
            if i >= len(books):
                break
            
            job += books[i]
            if record['min_global_max'] and job >= record['min_global_max']:
                break
            
            local_max = max(local_max, job)
            self.dfs(books, longest, i + 1, cut + 1, k, local_max, record)
