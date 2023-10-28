class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        zero_idx = -1
        total_product = 1

        for idx, num in enumerate(nums):
            if num == 0:
                if zero_cnt > 0:
                    return [0] * len(nums)
                zero_cnt += 1
                zero_idx = idx
            else:
                total_product *= num
        
        if zero_cnt == 1:
            ans = [0] * len(nums)
            ans[zero_idx] = total_product
            return ans

        ans = []
        for num in nums:
            ans.append(total_product // num)
        return ans
