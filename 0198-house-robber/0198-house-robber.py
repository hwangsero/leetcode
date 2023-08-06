class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.memory = [-1] * len(nums)
        return self.recursive_rub(0)
    
    def recursive_rub(self, idx):
        if idx >= len(self.nums):
            return 0

        if self.memory[idx] >= 0:
            return self.memory[idx]
        
        self.memory[idx] = max(self.nums[idx] + self.recursive_rub(idx + 2), self.recursive_rub(idx + 1))
        return self.memory[idx]

        
