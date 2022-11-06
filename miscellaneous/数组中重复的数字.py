class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                v = nums[i]
                if nums[v] == v:
                    return v
                nums[i], nums[v] = nums[v], nums[i]
