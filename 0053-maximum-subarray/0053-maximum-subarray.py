class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = cur_sum = nums[0]
        for i in range(1, len(nums)):
            if cur_sum + nums[i] > nums[i]:
                cur_sum += nums[i]
            elif cur_sum + nums[i] <= nums[i]:
                cur_sum = nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum
