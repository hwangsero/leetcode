class Solution:
    def canJump(self, nums: List[int]) -> bool:
        d = [-1] * (len(nums) + 1)
        def check(idx: int):
            if idx == len(nums) - 1:
                return True
            if idx >= len(nums) or d[idx] == 0:
                return False
            
            for next_idx in range(idx + nums[idx], idx, -1):
                current_result = check(next_idx)
                if current_result:
                    return True
            d[idx] = 0
            return False
        return check(0)
            
        

"""
- 현재 위치에서 가능한 모든 경우를 시도
- 특정 위치에서 가능 여부를 


"""