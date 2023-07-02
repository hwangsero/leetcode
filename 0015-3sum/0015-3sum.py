class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = set()

        for idx in range(n):
            if (idx > 0 and nums[idx - 1] == nums[idx]):
                continue

            left, right = idx + 1, n - 1
            while left < right:
                total = nums[left] + nums[right] + nums[idx]
                if  total == 0:
                    ans.add((nums[idx], nums[left], nums[right]))
                    left += 1
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
        return list(map(list,ans))
