class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(idx):
            if idx == len(nums):
                ans.append(combination[:])
                return

            dfs(idx + 1)
            combination.append(nums[idx])
            dfs(idx + 1)
            combination.pop()

        ans = []
        combination = []
        dfs(0)
        return ans
