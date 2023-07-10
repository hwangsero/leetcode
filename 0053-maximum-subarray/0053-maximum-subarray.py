class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_sum = max_sum = nums[0]
        for num in nums[1:]:
            pre_sum = max(num, pre_sum + num)
            max_sum = max(pre_sum, max_sum)
        return max_sum
