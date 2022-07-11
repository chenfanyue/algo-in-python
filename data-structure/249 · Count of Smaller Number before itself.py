from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def count_of_smaller_number_i_i(self, a: List[int]) -> List[int]:
        if not a:
            return []
        
        block_list = BlockList(10000)
        res = []

        for v in a:
            query = block_list.qeury(v)
            res.append(query)
            block_list.insert(v)
        
        return res


class Block:
    def __init__(self):
        self.total = 0
        self.cnt = {}

class BlockList:
    def __init__(self, capacity):
        self.block_size = int(math.sqrt(capacity))
        self.blocks = [
            Block()
            for _ in range(capacity // self.block_size + 1)
        ]

    def insert(self, val):
        block_idx = val // self.block_size
        block = self.blocks[block_idx]
        block.total += 1
        block.cnt[val] = block.cnt.get(val, 0) + 1
    
    def qeury(self, val):
        res = 0
        block_idx = val // self.block_size

        for i in range(block_idx):
            res += self.blocks[i].total
        
        block = self.blocks[block_idx]
        for v in block.cnt:
            if v < val:
                res += block.cnt[v]
        
        return res



