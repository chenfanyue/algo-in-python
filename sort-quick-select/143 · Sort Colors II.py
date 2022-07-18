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

        left, right = 0, len(colors) - 1
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
            
            left, right = right + 1, len(colors) - 1
