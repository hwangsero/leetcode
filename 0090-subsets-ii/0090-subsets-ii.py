class Solution:
    def subsetsWithDup(self, nums):
        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        nums = sorted(nums)
        res = []
        backtrack(0, [])
        return res

 
