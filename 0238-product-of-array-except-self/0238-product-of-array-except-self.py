from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # output 배열 초기화. 모든 값이 1이 되게끔.
        output = [1] * n
        
        # 왼쪽에서 오른쪽으로 곱해나가면서 output 업데이트
        left_product = 1
        for i in range(n):
            output[i] *= left_product
            left_product *= nums[i]
        
        # 오른쪽에서 왼쪽으로 곱해나가면서 output 업데이트
        right_product = 1
        for i in range(n-1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output