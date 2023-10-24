class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(cur: List[int]):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return

            for idx, num in enumerate(nums): 
                if check[idx] == 1:
                    continue
                check[idx] = 1
                cur.append(num)
                dfs(cur)
                cur.pop()
                check[idx] = 0
        ans = []
        check = [0] * len(nums)
        dfs([])
        return ans
