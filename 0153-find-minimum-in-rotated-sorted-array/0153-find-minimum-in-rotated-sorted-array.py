import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        min_val = sys.maxsize
        while left <= right:
            mid = (left + right) // 2

            min_val = min(min_val, nums[mid])
            if nums[left] <= nums[mid]:
                min_val = min(min_val, nums[left])
                left = mid + 1
            else:
                right = mid - 1
        return min_val
