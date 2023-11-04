from typing import List
import pytest
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()

        for idx, val in enumerate(nums):
            find_val = target - val
            if find_val in hash_table:
                return [hash_table[find_val], idx]
            hash_table[val] = idx
