class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(left: int, right: int):
            if left > right:
                return
            mid = (left + right) // 2

            if nums[mid] == target:
                self.min_idx = mid if self.min_idx == -1 else min(self.min_idx, mid)
                self.max_idx = mid if self.max_idx == -1 else max(self.max_idx, mid)
                binary_search(left, mid - 1)
                binary_search(mid + 1, right)
            elif nums[mid] > target:
                binary_search(left, mid - 1)
            elif nums[mid] < target:
                binary_search(mid + 1, right)
        self.min_idx = self.max_idx = -1
        binary_search(0, len(nums) - 1)
        return [self.min_idx, self.max_idx]
