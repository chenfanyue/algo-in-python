from typing import (
    List,
)

# quick select
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        if not colors:
            return

        left, right = 0, (end := len(colors) - 1)
        for pivot in range(2, k + 1):
            while left <= right:
                while left <= right and colors[left] < pivot:
                    left += 1
                while left <= right and colors[right] >= pivot:
                    right -= 1
                if left <= right:
                    colors[left], colors[right] = colors[right], colors[left]
                    left += 1
                    right -= 1
            
            right = end


# counting sort
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        if not colors:
            return

        cnt = [0] * (k + 1)
        for v in colors:
            cnt[v] += 1

        # res = []
        # for i in range(1, len(cnt)):
        #     res.extend([i] * cnt[i])
        idx = -1
        for v in range(1, k + 1):
            for _ in range(cnt[v]):
                idx += 1
                colors[idx] = v


# divide and conquer, 清晰分区
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        self.dfs(colors, 0, len(colors) - 1, 1, k)
        
    def dfs(self, colors, start, end, start_color, end_color):
        if start_color == end_color:
            return

        mid_color = (start_color + end_color) >> 1
        left, right = start, end # index
        while left <= right:
            while left <= right and colors[left] <= mid_color:
                left += 1
            while left <= right and colors[right] > mid_color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.dfs(colors, start, right, start_color, mid_color)
        self.dfs(colors, left, end, mid_color + 1, end_color)


